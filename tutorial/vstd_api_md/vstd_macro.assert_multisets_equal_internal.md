<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](index.html)

</div>

# Macro <span class="macro">assert_multisets_equal_internal</span> Copy item path

<span class="sub-heading"><a href="../src/vstd/multiset.rs.html#560-589" class="src">Source</a>
</span>

</div>

``` rust
macro_rules! assert_multisets_equal_internal {
    (::verus_builtin::spec_eq($m1:expr, $m2:expr)) => { ... };
    (::verus_builtin::spec_eq($m1:expr, $m2:expr), $k:ident $( : $t:ty )? => $bblock:block) => { ... };
    (crate::verus_builtin::spec_eq($m1:expr, $m2:expr)) => { ... };
    (crate::verus_builtin::spec_eq($m1:expr, $m2:expr), $k:ident $( : $t:ty )? => $bblock:block) => { ... };
    ($m1:expr, $m2:expr $(,)?) => { ... };
    ($m1:expr, $m2:expr, $k:ident $( : $t:ty )? => $bblock:block) => { ... };
}
```

</div>

</div>
