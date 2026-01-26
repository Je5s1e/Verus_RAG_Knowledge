<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[pervasive](index.html)

</div>

# Trait <span class="trait">ForLoopGhostIteratorNew</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/pervasive.rs.html#84-90" class="src">Source</a>
</span>

</div>

``` rust
pub trait ForLoopGhostIteratorNew {
    type GhostIter;
}
```

## Required Associated Types<a href="#required-associated-types" class="anchor">§</a>

<div class="methods">

<div id="associatedtype.GhostIter" class="section method">

<a href="../../src/vstd/pervasive.rs.html#85"
class="src rightside">Source</a>

#### type <a href="#associatedtype.GhostIter" class="associatedtype">GhostIter</a>

</div>

</div>

## Implementations on Foreign Types<a href="#foreign-impls" class="anchor">§</a>

<div id="impl-ForLoopGhostIteratorNew-for-Chars%3C'a%3E"
class="section impl">

<a href="../../src/vstd/string.rs.html#412-418"
class="src rightside">Source</a><a href="#impl-ForLoopGhostIteratorNew-for-Chars%3C&#39;a%3E"
class="anchor">§</a>

### impl\<'a\> <a href="trait.ForLoopGhostIteratorNew.html" class="trait"
title="trait vstd::pervasive::ForLoopGhostIteratorNew">ForLoopGhostIteratorNew</a> for <a
href="https://doc.rust-lang.org/1.92.0/core/str/iter/struct.Chars.html"
class="struct" title="struct core::str::iter::Chars">Chars</a>\<'a\>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `alloc`** only.

</div>

</div>

<div class="impl-items">

<div id="associatedtype.GhostIter-1"
class="section associatedtype trait-impl">

<a href="../../src/vstd/string.rs.html#413"
class="src rightside">Source</a><a href="#associatedtype.GhostIter-1" class="anchor">§</a>

#### type <a href="#associatedtype.GhostIter" class="associatedtype">GhostIter</a> = <a href="../string/struct.CharsGhostIterator.html" class="struct"
title="struct vstd::string::CharsGhostIterator">CharsGhostIterator</a>\<'a\>

</div>

</div>

## Implementors<a href="#implementors" class="anchor">§</a>

<div id="implementors-list">

</div>

</div>

</div>
