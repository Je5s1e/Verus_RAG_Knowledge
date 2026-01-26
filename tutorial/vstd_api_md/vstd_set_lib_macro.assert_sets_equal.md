<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[set_lib](index.html)

</div>

# Macro <span class="macro">assert_sets_equal</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/set_lib.rs.html#1299-1303"
class="src">Source</a> </span>

</div>

``` rust
macro_rules! assert_sets_equal {
    [$($tail:tt)*] => { ... };
}
```

Expand description

<div class="docblock">

Prove two sets equal by extensionality. Usage is:

<div class="example-wrap">

``` rust
assert_sets_equal!(set1 == set2);
```

</div>

or,

<div class="example-wrap">

``` rust
assert_sets_equal!(set1 == set2, elem => {
    // prove that set1.contains(elem) iff set2.contains(elem)
});
```

</div>

</div>

</div>

</div>
