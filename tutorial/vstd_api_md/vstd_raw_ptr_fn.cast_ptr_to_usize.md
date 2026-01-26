<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[raw_ptr](index.html)

</div>

# Function <span class="fn">cast_ptr_to_usize</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/raw_ptr.rs.html#521-528" class="src">Source</a>
</span>

</div>

``` rust
pub fn cast_ptr_to_usize<T: Sized>(ptr: *mut T) -> usize
```

Expand description

<div class="docblock">

Cast the address of a pointer to a `usize`.

Don’t call this directly; use an `as`-cast instead.

</div>

</div>

</div>
