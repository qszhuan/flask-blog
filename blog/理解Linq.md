##理解linq  
Category: C#  
Tags: linq, nhibernate  
Date: 2013-05-04  

最近在项目中遇到了一个数据库方面的性能问题。当页面需要显示User信息的时候，还会把User关联的HomeCountry, School和Relation信息显示出来。


<pre><code class="csharp">
public IEnumerable<Person> FindPersonByIdsWithOrder(List<long> ids)
{
    var entityList = BatchLoadByIds(ids,r => r
        .Fetch(a => a.HomeCountry)
        .FetchMany(a => a.Engagements)
        .FetchMany(a => a.Assignments));
}
        
protected IEnumerable<T> BatchLoadByIds(List<long> ids, Func<IQueryable<T>, IQueryable<T>> actionForFetch)
{
    var result = new List<T>(ids.Count);
    ids.Batch(SQL_SERVER_PARAMETER_LIMIT).ForEach(batch =>
    {
        var batchResult = actionForFetch(All().Where(t => batch.Contains(t.Id)));
        result.AddRange(batchResult);
    });
    return result;
}

</code></pre>




