<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[raw_ptr](index.html)

</div>

# Function <span class="fn">cast_ptr_to_thin_ptr</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/raw_ptr.rs.html#407-414" class="src">Source</a>
</span>

</div>

``` rust
pub fn cast_ptr_to_thin_ptr<T: ?Sized, U: Sized>(ptr: *mut T) -> *mut U
```

Expand description

<div class="docblock">

Cast a pointer to a thin pointer. Address and provenance are preserved;
metadata is now thin.

Don’t call this directly; use an `as`-cast instead.

</div>

</div>

</div>
