<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[raw_ptr](index.html)

</div>

# Function <span class="fn">ptr_ref</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/raw_ptr.rs.html#581-591" class="src">Source</a>
</span>

</div>

``` rust
pub fn ptr_ref<T>(ptr: *const T, verus_tmp_perm: Tracked<&PointsTo<T>>) -> &T
```

Expand description

<div class="docblock">

Equivalent to `&*ptr`, passing in a permission `perm` to ensure safety.
The memory pointed to by `ptr` must be initialized.

</div>

</div>

</div>
