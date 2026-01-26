<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[raw_ptr](index.html)

</div>

# Function <span class="fn">cast_slice_ptr_to_str_ptr</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/raw_ptr.rs.html#477-484" class="src">Source</a>
</span>

</div>

``` rust
pub fn cast_slice_ptr_to_str_ptr<T>(ptr: *mut [T]) -> *mut str
```

Expand description

<div class="docblock">

Cast a slice pointer to a `str` pointer. Length is preserved even if the
size of the elements changes.

Don’t call this directly; use an `as`-cast instead.

</div>

</div>

</div>
