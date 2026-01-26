<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[raw_ptr](index.html)

</div>

# Function <span class="fn">ptr_mut_read</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/raw_ptr.rs.html#563-575" class="src">Source</a>
</span>

</div>

``` rust
pub fn ptr_mut_read<T>(
    ptr: *const T,
    verus_tmp_perm: Tracked<&mut PointsTo<T>>,
) -> T
```

Expand description

<div class="docblock">

Calls
[`core::ptr::read`](https://doc.rust-lang.org/1.92.0/core/ptr/fn.read.html "fn core::ptr::read")
to read from the memory pointed to by `ptr`, using the permission
`perm`.

This leaves the data as “unitialized”, i.e., performs a move.

TODO: This needs to be made more general (i.e., should be able to read a
Copy type without destroying it; should be able to leave the bytes
intact without uninitializing them).

</div>

</div>

</div>
