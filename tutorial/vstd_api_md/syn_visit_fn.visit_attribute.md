<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[syn](../index.html)::[visit](index.html)

</div>

# Function <span class="fn">visit_attribute</span> Copy item path

<span class="sub-heading"><a href="../../src/syn/gen/visit.rs.html#1033-1041"
class="src">Source</a> </span>

</div>

``` rust
pub fn visit_attribute<'ast, V>(v: &mut V, node: &'ast Attribute)where
    V: Visit<'ast> + ?Sized,
```

</div>

</div>
