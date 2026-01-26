<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[slice](index.html)

</div>

# Trait <span class="trait">ExSliceIndex</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/slice.rs.html#116-120" class="src">Source</a>
</span>

</div>

``` rust
pub trait ExSliceIndex<T>where
    T: ?Sized,{
    type ExternalTraitSpecificationFor: SliceIndex<T>;
    type Output: ?Sized;
}
```

## Required Associated Types<a href="#required-associated-types" class="anchor">§</a>

<div class="methods">

<div id="associatedtype.ExternalTraitSpecificationFor"
class="section method">

<a href="../../src/vstd/slice.rs.html#117"
class="src rightside">Source</a>

#### type <a href="#associatedtype.ExternalTraitSpecificationFor"
class="associatedtype">ExternalTraitSpecificationFor</a>: <a
href="https://doc.rust-lang.org/1.92.0/core/slice/index/trait.SliceIndex.html"
class="trait"
title="trait core::slice::index::SliceIndex">SliceIndex</a>\<T\>

</div>

<div id="associatedtype.Output" class="section method">

<a href="../../src/vstd/slice.rs.html#119"
class="src rightside">Source</a>

#### type <a href="#associatedtype.Output" class="associatedtype">Output</a>: ?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>

</div>

</div>

## Implementors<a href="#implementors" class="anchor">§</a>

<div id="implementors-list">

</div>

</div>

</div>
