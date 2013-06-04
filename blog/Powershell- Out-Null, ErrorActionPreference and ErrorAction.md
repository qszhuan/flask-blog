##Powershell: Out-Null, ErrorActionPreference and ErrorAction
Category: PowerShell
Tags: ErrorAction, Out-Null, ErrorActionPreference, ErrorAction, ErrorVariable
Date: 2013-06-05

####Out-Null
If we want to discard the output instead of sending it to the console, usually we use `Out-Null` function. For example:

<pre><code class="ps1">
PS C:\> ls


    Directory: C:\


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
d----         7/14/2009  10:37 AM            PerfLogs
d-r--          5/8/2013  11:38 AM            Program Files
d-r--          5/8/2013  11:38 AM            Users
d----          5/8/2013  11:41 AM            Windows
-a---         6/11/2009   5:42 AM         24 autoexec.bat
-a---         6/11/2009   5:42 AM         10 config.sys


PS C:\> ls | out-null
PS C:\>
</code></pre>

This will not display the output of `ls` command in the console.
 
####$ErrorActionPreference
But there are still some cases that we can not delete the output in such way. 

<pre><code class="ps1">
PS C:\> kill -name whatever | out-null
Stop-Process : Cannot find a process with the name "whatever". Verify the process name and call the cmdlet again.
At line:1 char:5
+ kill <<<<  -name whatever
    + CategoryInfo          : ObjectNotFound: (whatever:String) [Stop-Process], ProcessCommandException
    + FullyQualifiedErrorId : NoProcessFoundForGivenName,Microsoft.PowerShell.Commands.StopProcessCommand

PS C:\>
</code></pre>

Why? Let's talk a little about the command pipeline, which uses the symbol `|` to pass output of the first clause as the input of the second one.

In the latter example, the error messages that displayed in the console is not the output of the command `kill -name whatever`, so it can not be discarded by the following `out-null` command.

So, how to discard the above error messages?

Type `man about_perference_variables` in powershell, you will get the following output:

<pre><code class="ps1">
PS C:\>  man about_preference_variables
TOPIC
    Preference Variables

SHORT DESCRIPTION
    Variables that customize the behavior of Windows PowerShell

LONG DESCRIPTION
    Windows PowerShell includes a set of variables that enable you to
    customize its behavior. These "preference variables" work like the
    options in GUI-based systems.

    The preference variables affect the Windows PowerShell operating
    environment and all commands run in the environment. In many cases,
    the cmdlets have parameters that you can use to override the preference
    behavior for a specific command.

    The following table lists the preference variables and their default
    values.

    Variable                             Default Value
    --------                             -------------
    $ConfirmPreference                   High
    $DebugPreference                     SilentlyContinue
    $ErrorActionPreference               Continue
    $ErrorView                           NormalView
    $FormatEnumerationLimit              4
    $LogCommandHealthEvent               False (not logged)
    $LogCommandLifecycleEvent            False (not logged)
    $LogEngineHealthEvent                True (logged)
    $LogEngineLifecycleEvent             True (logged)
    $LogProviderLifecycleEvent           True (logged)
    $LogProviderHealthEvent              True (logged)
    $MaximumAliasCount                   4096
    $MaximumDriveCount                   4096
    $MaximumErrorCount                   256
    $MaximumFunctionCount                4096
    $MaximumHistoryCount                 64
    $MaximumVariableCount                4096
    $OFS                                 (Space character (" "))
    $OutputEncoding                      ASCIIEncoding object
    $ProgressPreference                  Continue
    $PSEmailServer                       (None)
    $PSSessionApplicationName            WSMAN
    $PSSessionConfigurationName          http://schemas.microsoft.com/powershell/microsoft.powershell
    $PSSessionOption                     (See below)
    $VerbosePreference                   SilentlyContinue
    $WarningPreference                   Continue
    $WhatIfPreference                    0

</code></pre>

There is a parameter called **$ErrorActionPreference**, the default value of which is **Continue**.

Let's change it to **SilentlyContinue**, and try again.

<pre><code class="ps1">
PS C:\> $ErrorActionPreference
Continue
PS C:\> $ErrorActionPreference = 'silentlycontinue'
PS C:\> kill -name whatever
PS C:\>
</code></pre>

**Bingo!**

####-ErrorAction & -ErrorVariable
Let's go futher. Changing the value of **$ErrorActionPreference** will affect all the commands in current powershell console. What if I just want to discard the error message of specific command?

Type `man about_perference_variables` in powershell, you will get the following output:

<pre><code class="ps1">
PS C:\> man about_commonparameters
TOPIC
    about_CommonParameters

SHORT DESCRIPTION
    Describes the parameters that can be used with any cmdlet.


LONG DESCRIPTION
    The common parameters are a set of cmdlet parameters that you can
    use with any cmdlet. They are implemented by Windows PowerShell, not
    by the cmdlet developer, and they are automatically available to any
    cmdlet.


    You can use the common parameters with any cmdlet, but they might
    not have an effect on all cmdlets. For example, if a cmdlet does not
    generate any verbose output, using the Verbose common parameter
    has no effect.


    Several common parameters override system defaults or preferences
    that you set by using the Windows PowerShell preference variables. Unlike
    the preference variables, the common parameters affect only the commands
    in which they are used.


    In addition to the common parameters, many cmdlets offer the WhatIf and
    Confirm risk mitigation parameters. Cmdlets that involve risk to the system
    or to user data usually offer these parameters.


    The common parameters are:


       -Verbose
       -Debug
       -WarningAction
       -WarningVariable
       -ErrorAction
       -ErrorVariable
       -OutVariable
       -OutBuffer
   …………

    -ErrorAction[:{SilentlyContinue | Continue | Inquire | Stop)]

        Determines how the cmdlet responds to a non-terminating error
        from the command. This parameter works only when the command generates
        a debugging message. For example, this parameters works when a command
        contains the Write-Error cmdlet.

        The ErrorAction parameter overrides the value of the
        $ErrorActionPreference variable for the current command.
        Because the default value of the $ErrorActionPreference variable
        is Continue, error messages are displayed and execution continues
        unless you use the ErrorAction parameter.

        The ErrorAction parameter has no effect on terminating errors (such as
        missing data, parameters that are not valid, or insufficient
        permissions) that prevent a command from completing successfully.

        Valid values:

            SilentlyContinue. Suppresses the error message and continues
            executing the command.

            Continue. Displays the error message and continues executing
            the command. "Continue" is the default value.

            Inquire. Displays the error message and prompts you for
            confirmation before continuing execution. This value is rarely
            used.

            Stop. Displays the error message and stops executing the
            command.


    -ErrorVariable [+]<variable-name>

        Stores error messages about the command in the specified variable
        and in the $Error automatic variable. For more information,
        type the following command:

            get-help about_automatic_variables

        By default, new error messages overwrite error messages that are
        already stored in the variable. To append the error message to the
        variable content, type  a plus sign (+) before the variable name.

        For example, the following command creates the $a variable and then
        stores any errors in it:

            get-process -id 6 -ErrorVariable a

        The following command adds any error messages to the $a variable:


            get-process -id 2 -ErrorVariable +a

        The following command displays the contents of $a:

            $a

        You can use this parameter to create a variable that contains only
        error messages from specific commands. The $Error automatic
        variable contains error messages from all the commands in the session.
        You can use array notation, such as $a[0] or $error[1,2] to refer to
        specific errors stored in the variables.
   ……
</code></pre>

We only focus on the **-ErrorAction** and the **-ErrorVariable** now. It does't need to explain anymore, as the document is detailed. Try it ourselves:

<pre><code class="ps1">
PS C:\> $ErrorActionPreference
Continue
PS C:\> kill -name whatever  -ErrorAction SilentlyContinue -ErrorVariable a
PS C:\> kill -name nomatterwhat  -ErrorAction SilentlyContinue -ErrorVariable +a
PS C:\> $a
Stop-Process : Cannot find a process with the name "whatever". Verify the process name and call the cmdlet again.
At line:1 char:5
+ kill <<<<  -name whatever  -ErrorAction SilentlyContinue -ErrorVariable a
    + CategoryInfo          : ObjectNotFound: (whatever:String) [Stop-Process], ProcessCommandException
    + FullyQualifiedErrorId : NoProcessFoundForGivenName,Microsoft.PowerShell.Commands.StopProcessCommand

Stop-Process : Cannot find a process with the name "nomatterwhat". Verify the process name and call the cmdlet again.
At line:1 char:5
+ kill <<<<  -name nomatterwhat  -ErrorAction SilentlyContinue -ErrorVariable +a
    + CategoryInfo          : ObjectNotFound: (nomatterwhat:String) [Stop-Process], ProcessCommandException
    + FullyQualifiedErrorId : NoProcessFoundForGivenName,Microsoft.PowerShell.Commands.StopProcessCommand

PS C:\>

</code></pre>

But the **$ErrorActionPreference** can not totally replace **-ErrorAction**, as the **-ErrorAction** parameter has no effect on terminating errors, which is described in the documents. 

That's to say, `kill notapid -ErrorAction SilentlyContinue` does not work.

*BTW, you can use alias for short: **-EA** and **-EV**.*

