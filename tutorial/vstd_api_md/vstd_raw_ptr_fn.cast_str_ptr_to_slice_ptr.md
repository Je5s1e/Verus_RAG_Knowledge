<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[raw_ptr](index.html)

</div>

# Function <span class="fn">cast_str_ptr_to_slice_ptr</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/raw_ptr.rs.html#501-508" class="src">Source</a>
</span>

</div>

``` rust
pub fn cast_str_ptr_to_slice_ptr<T>(ptr: *mut str) -> *mut [T]
```

Expand description

<div class="docblock">

Cast a `str` pointer to a slice pointer. Length is preserved even if the
size of the elements changes.

Don’t call this directly; use an `as`-cast instead.

</div>

</div>

</div>
