<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[raw_ptr](index.html)

</div>

# Function <span class="fn">allocate</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/raw_ptr.rs.html#864-893" class="src">Source</a>
</span>

</div>

``` rust
pub fn allocate(
    size: usize,
    align: usize,
) -> (*mut u8, Tracked<PointsToRaw>, Tracked<Dealloc>)
```

Expand description

<div class="docblock">

Allocate with the global allocator. The precondition should be
consistent with the [documented safety conditions on
`alloc`](https://doc.rust-lang.org/alloc/alloc/trait.GlobalAlloc.html#tymethod.alloc).
Returns a pointer with a corresponding
[`PointsToRaw`](struct.PointsToRaw.html "struct vstd::raw_ptr::PointsToRaw")
and [`Dealloc`](struct.Dealloc.html "struct vstd::raw_ptr::Dealloc")
permissions.

</div>

</div>

</div>
