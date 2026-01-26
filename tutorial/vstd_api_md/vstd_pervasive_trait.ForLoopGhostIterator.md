<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[pervasive](index.html)

</div>

# Trait <span class="trait">ForLoopGhostIterator</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/pervasive.rs.html#42-82" class="src">Source</a>
</span>

</div>

``` rust
pub trait ForLoopGhostIterator {
    type ExecIter;
    type Item;
    type Decrease;
}
```

## Required Associated Types<a href="#required-associated-types" class="anchor">§</a>

<div class="methods">

<div id="associatedtype.ExecIter" class="section method">

<a href="../../src/vstd/pervasive.rs.html#43"
class="src rightside">Source</a>

#### type <a href="#associatedtype.ExecIter" class="associatedtype">ExecIter</a>

</div>

<div id="associatedtype.Item" class="section method">

<a href="../../src/vstd/pervasive.rs.html#45"
class="src rightside">Source</a>

#### type <a href="#associatedtype.Item" class="associatedtype">Item</a>

</div>

<div id="associatedtype.Decrease" class="section method">

<a href="../../src/vstd/pervasive.rs.html#47"
class="src rightside">Source</a>

#### type <a href="#associatedtype.Decrease" class="associatedtype">Decrease</a>

</div>

</div>

## Implementors<a href="#implementors" class="anchor">§</a>

<div id="implementors-list">

<div id="impl-ForLoopGhostIterator-for-CharsGhostIterator%3C'a%3E"
class="section impl">

<a href="../../src/vstd/string.rs.html#421-460"
class="src rightside">Source</a><a href="#impl-ForLoopGhostIterator-for-CharsGhostIterator%3C&#39;a%3E"
class="anchor">§</a>

### impl\<'a\> <a href="trait.ForLoopGhostIterator.html" class="trait"
title="trait vstd::pervasive::ForLoopGhostIterator">ForLoopGhostIterator</a> for <a href="../string/struct.CharsGhostIterator.html" class="struct"
title="struct vstd::string::CharsGhostIterator">CharsGhostIterator</a>\<'a\>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `alloc`** only.

</div>

</div>

<div class="impl-items">

<div id="associatedtype.ExecIter-1"
class="section associatedtype trait-impl">

<a href="../../src/vstd/string.rs.html#422"
class="src rightside">Source</a><a href="#associatedtype.ExecIter-1" class="anchor">§</a>

#### type <a href="#associatedtype.ExecIter" class="associatedtype">ExecIter</a> = <a
href="https://doc.rust-lang.org/1.92.0/core/str/iter/struct.Chars.html"
class="struct" title="struct core::str::iter::Chars">Chars</a>\<'a\>

</div>

<div id="associatedtype.Item-1"
class="section associatedtype trait-impl">

<a href="../../src/vstd/string.rs.html#424"
class="src rightside">Source</a><a href="#associatedtype.Item-1" class="anchor">§</a>

#### type <a href="#associatedtype.Item" class="associatedtype">Item</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.char.html"
class="primitive">char</a>

</div>

<div id="associatedtype.Decrease-1"
class="section associatedtype trait-impl">

<a href="../../src/vstd/string.rs.html#426"
class="src rightside">Source</a><a href="#associatedtype.Decrease-1" class="anchor">§</a>

#### type <a href="#associatedtype.Decrease" class="associatedtype">Decrease</a> = <a href="../prelude/struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

</div>

</div>

</div>

</div>

</div>
