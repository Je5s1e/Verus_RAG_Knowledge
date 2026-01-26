<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[raw_ptr](index.html)

</div>

# Function <span class="fn">deallocate</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/raw_ptr.rs.html#904-925" class="src">Source</a>
</span>

</div>

``` rust
pub fn deallocate(
    p: *mut u8,
    size: usize,
    align: usize,
    verus_tmp_pt: Tracked<PointsToRaw>,
    verus_tmp_dealloc: Tracked<Dealloc>,
)
```

Expand description

<div class="docblock">

Deallocate with the global allocator.

The [`Dealloc`](struct.Dealloc.html "struct vstd::raw_ptr::Dealloc")
permission ensures that the [documented safety conditions on
`dealloc`](https://doc.rust-lang.org/1.82.0/core/alloc/trait.GlobalAlloc.html#tymethod.dealloc)
are satisfied; by also giving up permission of the
[`PointsToRaw`](struct.PointsToRaw.html "struct vstd::raw_ptr::PointsToRaw")
permission, we ensure there can be no use-after-free bug as a result of
this deallocation. In order to do so, the parameters of the
[`PointsToRaw`](struct.PointsToRaw.html "struct vstd::raw_ptr::PointsToRaw")
and [`Dealloc`](struct.Dealloc.html "struct vstd::raw_ptr::Dealloc")
permissions must match the parameters of the deallocation.

</div>

</div>

</div>
