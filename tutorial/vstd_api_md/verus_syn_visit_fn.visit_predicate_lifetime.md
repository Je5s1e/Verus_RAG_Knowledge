<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[verus_syn](../index.html)::[visit](index.html)

</div>

# Function <span class="fn">visit_predicate_lifetime</span> Copy item path

<span class="sub-heading"><a href="../../src/verus_syn/gen/visit.rs.html#4200-4210"
class="src">Source</a> </span>

</div>

``` rust
pub fn visit_predicate_lifetime<'ast, V>(
    v: &mut V,
    node: &'ast PredicateLifetime,
)where
    V: Visit<'ast> + ?Sized,
```

</div>

</div>
