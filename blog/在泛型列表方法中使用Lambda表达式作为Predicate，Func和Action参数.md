##[译]在泛型列表方法中使用Lambda表达式作为Predicate，Func和Action参数
Category: C#  
Tags: lambda,expression,generic,list,dotnet,.net,linq  
Date: 2013-05-04  



####简介

自从.NET泛型出现后，我在工作的项目中用泛型列表完成了很多的工作，它们是对对象进行存储，检索和其他一般操作的非常好的方式。泛型列表类的大多数方法将Predicate，Func，或者Action作为其参数。一开始这会让人有点疑惑。这篇文章旨在消除疑惑并让你通过在这三种类型参数中使用lambda表达式让你的代码更加的优雅。

如果你是lambda表达式新手，请看微软的这篇文章：
 
[http://msdn.microsoft.com/en-us/library/bb397687.aspx](http://msdn.microsoft.com/en-us/library/bb397687.aspx)


这是本文介绍的三种类型的简单定义：

* `Predicate` 一种委托，带参数，并且参数在代码块中被使用，永远返回布尔类型
* `Func`      一种委托，带参数，并且参数在代码块中被使用，返回类型可以自定义
* `Action`    一种委托，带参数，并且参数在代码块中被使用，无返回值

对于泛型列表，这些参数可以使程序员对列表中的每个元素执行一个方法。


####Common Code

本文的所有例子使用同一份的公共代码，以下是业务实体：

<pre><code class="csharp">
public class InventoryItem
{
    public int ID { get; set; }
    public int NumberInStock { get; set; }
    public double UnitCost { get; set; }
}
</code></pre>

这是使用的列表成员变量。

<pre><code class="csharp">
private List<InventoryItem> _inventoryList = new List<InventoryItem>();
</code></pre>


这是列表中存储的内容：

![image](http://www.intertech.com/PostingImages/4e517060d216_1260F/Contents.png)


####带Predicate参数的列表方法

泛型列表类的`Find`方法是一个使用Predicate作为参数的例子。为了创建一个Predicate类，让我们先看看一个典型的查找是如何完成的。对于我而言，`foreach`方法是我最好的朋友，无论我是使用泛型列表，ArrayList或是其他任何数据结构。例子如下：

<pre><code class="csharp">
public InventoryItem FindInventoryForeach(int inventoryID)
{
    foreach (InventoryItem item in _inventoryList)
    {
        if (item.ID == inventoryID)
            return item;
    }

    return null;
}
</code></pre>


现在，有一个更好的方式来完成这个一般性工作。泛型列表类通过一个内置的`Find`方法来实现它。传给`Find`方法的参数是泛型类。还记得Predicate的简单定义吧：*“一种委托，带参数，并且参数在代码块中被使用，永远返回布尔类型”*。在C#中，一个内联的委托创建一个匿名方法，这可以被赋值给Predicate变量。Predicate变量然后就可以像下面这样传给`Find`方法：

<pre><code class="csharp">
public InventoryItem FindInventoryPredicateDelegate(int inventoryID)
{
    Predicate<InventoryItem> pred = delegate(InventoryItem item)
    {
        return item.ID == inventoryID;
    };

    return _inventoryList.Find(pred);
}
</code></pre>

如果你想保存委托并重用，这非常有用。当然委托也可以简单地传给`Find`方法，如下：

<pre><code class="csharp">
public InventoryItem FindInventoryDelegate(int inventoryID)
{
    return _inventoryList.Find(delegate(InventoryItem item)
    {
        return item.ID == inventoryID;
    });
}
</code></pre>

正则表达式简化了上述代码。这是一个使用lambda表达式的Predicate的例子，在“=”右边是lambda表达式。

<pre><code class="csharp">
public InventoryItem FindInventoryPredicateLambda(int inventoryID)
{
    Predicate<InventoryItem> pred = item => item.ID == inventoryID;

    return _inventoryList.Find(pred);
}
</code></pre>

正则表达式可以读作“符合其ID == inventoryID的元素”。换句话说，元素是”=>"右边的参数。Predicate变量仍然可以重用。在我看来，使用lambda表达式看起来更整洁。进一步简化，Predicate变量支持以lambda表达式的形式直接传给`Find`方法，如下：

<pre><code class="csharp">
public InventoryItem FindInventory(int inventoryID)
{
    return _inventoryList.Find(item => item.ID == inventoryID);
}
</code></pre>

The preceding Find examples all output the same with an inventoryID of 5 as shown:

![image](http://www.intertech.com/PostingImages/4e517060d216_1260F/FindOutput.png)

**下述带Predicate参数的泛型列表方法也很有用:**

* `FindAll` - 返回符合条件的对象列表
* `RemoveAll` - 移除符合条件的对象
* `Exists` - 是否存在符合条件的对象存在？
* `FindLast` - 返回符合条件的最末一个对象

完整列表请参见 [http://msdn.microsoft.com/en-us/library/s6hkc2c4.aspx ](http://msdn.microsoft.com/en-us/library/s6hkc2c4.aspx)

####带Func参数的列表方法
有许多列表方法带Func类型参数。还记得Func的简单定义吧：“一种委托，带参数，并且参数在代码块中被使用，返回类型可以自定义”。Func比Predicate更灵活，因为它可以返回任何类型，而不仅仅是布尔值。有些Func带一个参数，有些带多个，取决于列表方法。

一个更有用的List方法叫`Where`，实际上是Enumerable的扩展方法。考虑一下使用此方法的SQL WHERE子句。它允许你得到一个Where Func指定的列表子集。下面是使用delegate的例子：

<pre><code class="csharp">
public List<InventoryItem> FindItemsWhereLessThanCostFuncDelegate(double unitCost)
{
    Func<InventoryItem, bool> whereFunc = delegate(InventoryItem item)
    {
        return item.UnitCost < unitCost;
    };

    return _inventoryList.Where(whereFunc).ToList<InventoryItem>();
}
</code></pre>

既然这里要返回一个InventoryItem的列表，你必须调用`ToList`因为Where返回一个IEnumerable，直到结果被枚举时查询才会执行。

上述例子能用Lambda表达式进行简化：

<pre><code class="csharp">
public List<InventoryItem> FindItemsWhereLessThanCostFuncLambda(double unitCost)
{
    Func<InventoryItem, bool> whereFunc = item => item.UnitCost < unitCost;

    return _inventoryList.Where(whereFunc).ToList<InventoryItem>();
}
</code></pre>

同样，这里的写法主要是在其他代码中重用Func。最好的简化是简单的直接向`Where`方法传递一个lambda表达式，如下：

<pre><code class="csharp">
public List<InventoryItem> FindItemsWhereLessThanCost(double unitCost)
{
    return _inventoryList.Where(item => item.UnitCost < unitCost)
        .ToList<InventoryItem>();
}
</code></pre>

上述Where的例子输出相同的unitCost为2.0的值。

![image](http://www.intertech.com/PostingImages/4e517060d216_1260F/WhereOutput.png)

下面的泛型列表方法有Func参数，也很有用：

* `FirstOrDefault` - 返回满足条件的第一个元素，或者返回一个默认值（对于对象，默认值为null）
* `LastOrDefault` - 返回满足条件的最末一个元素，或者返回一个默认值（对于对象，默认值为null）
* `First` - 返回满足条件的第一个元素

完整列表参见： [http://msdn.microsoft.com/en-us/library/s6hkc2c4.aspx](http://msdn.microsoft.com/en-us/library/s6hkc2c4.aspx) 

####带Action参数的列表方法
还记得Action的简单定义吧：*“一种委托，带参数，并且参数在代码块中被使用，无返回值”*。泛型列表类中有一个方法`ForEach`带Action参数。作用是对列表中的每一个元素执行你指定的代码。

在下面的例子中，对每一个inventory元素unit cost被设置成相同的值（单独的Action变量也可以通过委托或lambda表达式创建，然后传给`ForEach`方法）：

<pre><code class="csharp">
public void UnifyUnitCost(double unitCost)
{
    _inventoryList.ForEach(item => item.UnitCost = unitCost);
}
</code></pre>

输出下面的结果：

![image](http://www.intertech.com/PostingImages/4e517060d216_1260F/WhereOutput.png)

当然我也可以用`ForEach`命令输出结果：

<pre><code class="csharp">
helper.InventoryList.ForEach(item => Console.WriteLine(
    "item ID={0}, unit cost = {1}",
    item.ID.ToString(), item.UnitCost.ToString("C")));
</code></pre>

####结论

泛型列表类及其扩展有一些非常强大的方法，可以帮助你干一般性的工作。其中许多带Predicate，Func或者Action参数。最
简洁优雅的使用方法是向这类方法传递lambda表达式，LINQ非常重要的一部分。



参见[原文链接]

[原文链接]: http://www.intertech.com/Blog/Post/Using-Lambda-Expressions-for-Predicate-Func-and-Action-Arguments-in-Generic-List-Methods.aspx