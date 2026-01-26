<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[raw_ptr](index.html)

</div>

# Function <span class="fn">ptr_mut_write</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/raw_ptr.rs.html#540-552" class="src">Source</a>
</span>

</div>

``` rust
pub fn ptr_mut_write<T>(
    ptr: *mut T,
    verus_tmp_perm: Tracked<&mut PointsTo<T>>,
    v: T,
)
```

Expand description

<div class="docblock">

Calls
[`core::ptr::write`](https://doc.rust-lang.org/1.92.0/core/ptr/fn.write.html "fn core::ptr::write")
to write the value `v` to the memory location pointed to by `ptr`, using
the permission `perm`.

This does *not* drop the contents. If the memory is already initialized,
this could leak allocations or resources, so care should be taken to not
overwrite an object that should be dropped. This is appropriate for
initializing uninitialized memory, or overwriting memory that has
previously been
[read](fn.ptr_mut_read.html "fn vstd::raw_ptr::ptr_mut_read") from.

</div>

</div>

</div>
