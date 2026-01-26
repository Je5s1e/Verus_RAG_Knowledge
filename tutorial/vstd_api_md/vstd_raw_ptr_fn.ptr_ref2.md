<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[raw_ptr](index.html)

</div>

# Function <span class="fn">ptr_ref2</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/raw_ptr.rs.html#994-1009" class="src">Source</a>
</span>

</div>

``` rust
pub fn ptr_ref2<'a, T>(
    ptr: *const T,
    verus_tmp_perm: Tracked<&PointsTo<T>>,
) -> SharedReference<'a, T>
```

Expand description

<div class="docblock">

Like [`ptr_ref`](fn.ptr_ref.html "fn vstd::raw_ptr::ptr_ref") but
returns a `SharedReference` so it keeps track of the relationship
between the pointers. Note the resulting reference’s pointers does NOT
have the same provenance. This is because in Rust models like Stacked
Borrows / Tree Borrows, the pointer gets a new tag.

</div>

</div>

</div>
