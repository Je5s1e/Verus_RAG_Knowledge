<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[raw_ptr](index.html)

</div>

# Function <span class="fn">with_exposed_provenance</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/raw_ptr.rs.html#705-717" class="src">Source</a>
</span>

</div>

``` rust
pub fn with_exposed_provenance<T: Sized>(
    addr: usize,
    verus_tmp_provenance: Tracked<IsExposed>,
) -> *mut T
```

Expand description

<div class="docblock">

Construct a pointer with the given provenance from a *usize* address.
The provenance must have previously been exposed.

</div>

</div>

</div>
