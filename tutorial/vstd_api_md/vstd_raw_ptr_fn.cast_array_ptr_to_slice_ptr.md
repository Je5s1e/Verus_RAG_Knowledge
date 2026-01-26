<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[raw_ptr](index.html)

</div>

# Function <span class="fn">cast_array_ptr_to_slice_ptr</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/raw_ptr.rs.html#429-436" class="src">Source</a>
</span>

</div>

``` rust
pub fn cast_array_ptr_to_slice_ptr<T, const N: usize>(
    ptr: *mut [T; N],
) -> *mut [T]
```

Expand description

<div class="docblock">

Cast a pointer to an array of length `N` to a slice pointer. Address and
provenance are preserved; metadata has length `N`.

Don’t call this directly; use an `as`-cast instead.

</div>

</div>

</div>
