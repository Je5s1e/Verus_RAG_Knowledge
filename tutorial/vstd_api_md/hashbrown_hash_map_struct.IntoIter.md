<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[hashbrown](../index.html)::[hash_map](index.html)

</div>

# Struct <span class="struct">IntoIter</span> Copy item path

<span class="sub-heading"><a href="../../src/hashbrown/map.rs.html#2322-2324"
class="src">Source</a> </span>

</div>

``` rust
pub struct IntoIter<K, V, A: Allocator + Clone = Global> { /* private fields */ }
```

Expand description

<div class="docblock">

An owning iterator over the entries of a `HashMap` in arbitrary order.
The iterator element type is `(K, V)`.

This `struct` is created by the
[`into_iter`](struct.HashMap.html#method.into_iter) method on
[`HashMap`](struct.HashMap.html) (provided by the
[`IntoIterator`](https://doc.rust-lang.org/core/iter/trait.IntoIterator.html)
trait). See its documentation for more. The map cannot be used after
calling that method.

## <a href="#examples" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let map: HashMap<_, _> = [(1, "a"), (2, "b"), (3, "c")].into();

let mut iter = map.into_iter();
let mut vec = vec![iter.next(), iter.next(), iter.next()];

// The `IntoIter` iterator produces items in arbitrary order, so the
// items must be sorted to test them against a sorted array.
vec.sort_unstable();
assert_eq!(vec, [Some((1, "a")), Some((2, "b")), Some((3, "c"))]);

// It is fused iterator
assert_eq!(iter.next(), None);
assert_eq!(iter.next(), None);
```

</div>

</div>

## Trait Implementations<a href="#trait-implementations" class="anchor">§</a>

<div id="trait-implementations-list">

<div id="impl-Debug-for-IntoIter%3CK,+V,+A%3E" class="section impl">

<a href="../../src/hashbrown/map.rs.html#4754-4758"
class="src rightside">Source</a><a href="#impl-Debug-for-IntoIter%3CK,+V,+A%3E" class="anchor">§</a>

### impl\<K: <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a>, V: <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a>, A: Allocator + <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a> for <a href="struct.IntoIter.html" class="struct"
title="struct hashbrown::hash_map::IntoIter">IntoIter</a>\<K, V, A\>

</div>

<div class="impl-items">

<div id="method.fmt" class="section method trait-impl">

<a href="../../src/hashbrown/map.rs.html#4755-4757"
class="src rightside">Source</a><a href="#method.fmt" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html#tymethod.fmt"
class="fn">fmt</a>(&self, f: &mut <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/struct.Formatter.html"
class="struct" title="struct core::fmt::Formatter">Formatter</a>\<'\_\>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/type.Result.html"
class="type" title="type core::fmt::Result">Result</a>

</div>

<div class="docblock">

Formats the value using the given formatter. [Read
more](https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html#tymethod.fmt)

</div>

</div>

<div id="impl-ExactSizeIterator-for-IntoIter%3CK,+V,+A%3E"
class="section impl">

<a href="../../src/hashbrown/map.rs.html#4746-4751"
class="src rightside">Source</a><a href="#impl-ExactSizeIterator-for-IntoIter%3CK,+V,+A%3E"
class="anchor">§</a>

### impl\<K, V, A: Allocator + <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/exact_size/trait.ExactSizeIterator.html"
class="trait"
title="trait core::iter::traits::exact_size::ExactSizeIterator">ExactSizeIterator</a> for <a href="struct.IntoIter.html" class="struct"
title="struct hashbrown::hash_map::IntoIter">IntoIter</a>\<K, V, A\>

</div>

<div class="impl-items">

<div id="method.len" class="section method trait-impl">

<a href="../../src/hashbrown/map.rs.html#4748-4750"
class="src rightside">Source</a><a href="#method.len" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/exact_size/trait.ExactSizeIterator.html#method.len"
class="fn">len</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>

</div>

<div class="docblock">

Returns the exact remaining length of the iterator. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/exact_size/trait.ExactSizeIterator.html#method.len)

</div>

<div id="method.is_empty" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/exact_size.rs.html#148"
class="src rightside">Source</a><a href="#method.is_empty" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/exact_size/trait.ExactSizeIterator.html#method.is_empty"
class="fn">is_empty</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>

</div>

<span class="item-info"></span>

<div class="stab unstable">

🔬This is a nightly-only experimental API. (`exact_size_is_empty`)

</div>

<div class="docblock">

Returns `true` if the iterator is empty. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/exact_size/trait.ExactSizeIterator.html#method.is_empty)

</div>

</div>

<div id="impl-Iterator-for-IntoIter%3CK,+V,+A%3E" class="section impl">

<a href="../../src/hashbrown/map.rs.html#4734-4745"
class="src rightside">Source</a><a href="#impl-Iterator-for-IntoIter%3CK,+V,+A%3E" class="anchor">§</a>

### impl\<K, V, A: Allocator + <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html"
class="trait"
title="trait core::iter::traits::iterator::Iterator">Iterator</a> for <a href="struct.IntoIter.html" class="struct"
title="struct hashbrown::hash_map::IntoIter">IntoIter</a>\<K, V, A\>

</div>

<div class="impl-items">

<div id="associatedtype.Item" class="section associatedtype trait-impl">

<a href="../../src/hashbrown/map.rs.html#4735"
class="src rightside">Source</a><a href="#associatedtype.Item" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype">Item</a> = <a href="https://doc.rust-lang.org/1.92.0/core/primitive.tuple.html"
class="primitive">(K, V)</a>

</div>

<div class="docblock">

The type of the elements being iterated over.

</div>

<div id="method.next" class="section method trait-impl">

<a href="../../src/hashbrown/map.rs.html#4738-4740"
class="src rightside">Source</a><a href="#method.next" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#tymethod.next"
class="fn">next</a>(&mut self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="https://doc.rust-lang.org/1.92.0/core/primitive.tuple.html"
class="primitive">(K, V)</a>\>

</div>

<div class="docblock">

Advances the iterator and returns the next value. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#tymethod.next)

</div>

<div id="method.size_hint" class="section method trait-impl">

<a href="../../src/hashbrown/map.rs.html#4742-4744"
class="src rightside">Source</a><a href="#method.size_hint" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.size_hint"
class="fn">size_hint</a>(&self) -\> (<a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>, <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>\>)

</div>

<div class="docblock">

Returns the bounds on the remaining length of the iterator. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.size_hint)

</div>

<div id="method.next_chunk" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#110-114"
class="src rightside">Source</a><a href="#method.next_chunk" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.next_chunk"
class="fn">next_chunk</a>\<const N: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>\>( &mut self, ) -\> <a href="https://doc.rust-lang.org/1.92.0/core/result/enum.Result.html"
class="enum" title="enum core::result::Result">Result</a>\<\[Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>; <a href="https://doc.rust-lang.org/1.92.0/core/primitive.array.html"
class="primitive">N</a>\], <a
href="https://doc.rust-lang.org/1.92.0/core/array/iter/struct.IntoIter.html"
class="struct" title="struct core::array::iter::IntoIter">IntoIter</a>\<Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>, N\>\>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<span class="item-info"></span>

<div class="stab unstable">

🔬This is a nightly-only experimental API. (`iter_next_chunk`)

</div>

<div class="docblock">

Advances the iterator and returns an array containing the next `N`
values. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.next_chunk)

</div>

<div id="method.count" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#222-224"
class="src">Source</a></span><a href="#method.count" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.count"
class="fn">count</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Consumes the iterator, counting the number of iterations and returning
it. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.count)

</div>

<div id="method.last" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#250-252"
class="src">Source</a></span><a href="#method.last" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.last"
class="fn">last</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>\>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Consumes the iterator, returning the last element. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.last)

</div>

<div id="method.advance_by" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#297"
class="src rightside">Source</a><a href="#method.advance_by" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.advance_by"
class="fn">advance_by</a>(&mut self, n: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/result/enum.Result.html"
class="enum" title="enum core::result::Result">Result</a>\<<a href="https://doc.rust-lang.org/1.92.0/core/primitive.unit.html"
class="primitive">()</a>, <a
href="https://doc.rust-lang.org/1.92.0/core/num/nonzero/struct.NonZero.html"
class="struct" title="struct core::num::nonzero::NonZero">NonZero</a>\<<a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>\>\>

</div>

<span class="item-info"></span>

<div class="stab unstable">

🔬This is a nightly-only experimental API. (`iter_advance_by`)

</div>

<div class="docblock">

Advances the iterator by `n` elements. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.advance_by)

</div>

<div id="method.nth" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#374"
class="src">Source</a></span><a href="#method.nth" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.nth"
class="fn">nth</a>(&mut self, n: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>\>

</div>

<div class="docblock">

Returns the `n`th element of the iterator. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.nth)

</div>

<div id="method.step_by" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.28.0">1.28.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#424-426"
class="src">Source</a></span><a href="#method.step_by" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.step_by"
class="fn">step_by</a>(self, step: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>) -\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/adapters/step_by/struct.StepBy.html"
class="struct"
title="struct core::iter::adapters::step_by::StepBy">StepBy</a>\<Self\>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Creates an iterator starting at the same point, but stepping by the
given amount at each iteration. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.step_by)

</div>

<div id="method.chain" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#495-498"
class="src">Source</a></span><a href="#method.chain" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.chain"
class="fn">chain</a>\<U\>(self, other: U) -\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/adapters/chain/struct.Chain.html"
class="struct"
title="struct core::iter::adapters::chain::Chain">Chain</a>\<Self, \<U as <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.IntoIter"
class="associatedtype"
title="type core::iter::traits::collect::IntoIterator::IntoIter">IntoIter</a>\>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, U: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>\<Item
= Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>\>,

</div>

</div>

<div class="docblock">

Takes two iterators and creates a new iterator over both in sequence.
[Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.chain)

</div>

<div id="method.zip" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#613-616"
class="src">Source</a></span><a href="#method.zip" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.zip"
class="fn">zip</a>\<U\>(self, other: U) -\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/adapters/zip/struct.Zip.html"
class="struct" title="struct core::iter::adapters::zip::Zip">Zip</a>\<Self, \<U as <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.IntoIter"
class="associatedtype"
title="type core::iter::traits::collect::IntoIterator::IntoIter">IntoIter</a>\>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, U: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>,

</div>

</div>

<div class="docblock">

‘Zips up’ two iterators into a single iterator of pairs. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.zip)

</div>

<div id="method.intersperse" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#656-659"
class="src rightside">Source</a><a href="#method.intersperse" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.intersperse"
class="fn">intersperse</a>(self, separator: Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>) -\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/adapters/intersperse/struct.Intersperse.html"
class="struct"
title="struct core::iter::adapters::intersperse::Intersperse">Intersperse</a>\<Self\>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>:
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>,

</div>

</div>

<span class="item-info"></span>

<div class="stab unstable">

🔬This is a nightly-only experimental API. (`iter_intersperse`)

</div>

<div class="docblock">

Creates a new iterator which places a copy of `separator` between
adjacent items of the original iterator. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.intersperse)

</div>

<div id="method.intersperse_with" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#714-717"
class="src rightside">Source</a><a href="#method.intersperse_with" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.intersperse_with"
class="fn">intersperse_with</a>\<G\>(self, separator: G) -\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/adapters/intersperse/struct.IntersperseWith.html"
class="struct"
title="struct core::iter::adapters::intersperse::IntersperseWith">IntersperseWith</a>\<Self, G\>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, G: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>() -\>
Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>,

</div>

</div>

<span class="item-info"></span>

<div class="stab unstable">

🔬This is a nightly-only experimental API. (`iter_intersperse`)

</div>

<div class="docblock">

Creates a new iterator which places an item generated by `separator`
between adjacent items of the original iterator. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.intersperse_with)

</div>

<div id="method.map" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#773-776"
class="src">Source</a></span><a href="#method.map" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.map"
class="fn">map</a>\<B, F\>(self, f: F) -\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/adapters/map/struct.Map.html"
class="struct" title="struct core::iter::adapters::map::Map">Map</a>\<Self, F\>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>) -\>
B,

</div>

</div>

<div class="docblock">

Takes a closure and creates an iterator which calls that closure on each
element. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.map)

</div>

<div id="method.for_each" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.21.0">1.21.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#818-821"
class="src">Source</a></span><a href="#method.for_each" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.for_each"
class="fn">for_each</a>\<F\>(self, f: F)

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>),

</div>

</div>

<div class="docblock">

Calls a closure on each element of an iterator. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.for_each)

</div>

<div id="method.filter" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#893-896"
class="src">Source</a></span><a href="#method.filter" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.filter"
class="fn">filter</a>\<P\>(self, predicate: P) -\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/adapters/filter/struct.Filter.html"
class="struct"
title="struct core::iter::adapters::filter::Filter">Filter</a>\<Self, P\>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, P: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(&Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>) -\>
<a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>,

</div>

</div>

<div class="docblock">

Creates an iterator which uses a closure to determine if an element
should be yielded. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.filter)

</div>

<div id="method.filter_map" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#938-941"
class="src">Source</a></span><a href="#method.filter_map" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.filter_map"
class="fn">filter_map</a>\<B, F\>(self, f: F) -\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/adapters/filter_map/struct.FilterMap.html"
class="struct"
title="struct core::iter::adapters::filter_map::FilterMap">FilterMap</a>\<Self, F\>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>) -\>
<a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<B\>,

</div>

</div>

<div class="docblock">

Creates an iterator that both filters and maps. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.filter_map)

</div>

<div id="method.enumerate" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#985-987"
class="src">Source</a></span><a href="#method.enumerate" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.enumerate"
class="fn">enumerate</a>(self) -\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/adapters/enumerate/struct.Enumerate.html"
class="struct"
title="struct core::iter::adapters::enumerate::Enumerate">Enumerate</a>\<Self\>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Creates an iterator which gives the current iteration count as well as
the next value. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.enumerate)

</div>

<div id="method.peekable" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#1056-1058"
class="src">Source</a></span><a href="#method.peekable" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.peekable"
class="fn">peekable</a>(self) -\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/adapters/peekable/struct.Peekable.html"
class="struct"
title="struct core::iter::adapters::peekable::Peekable">Peekable</a>\<Self\>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Creates an iterator which can use the
[`peek`](https://doc.rust-lang.org/1.92.0/core/iter/adapters/peekable/struct.Peekable.html#method.peek "method core::iter::adapters::peekable::Peekable::peek")
and
[`peek_mut`](https://doc.rust-lang.org/1.92.0/core/iter/adapters/peekable/struct.Peekable.html#method.peek_mut "method core::iter::adapters::peekable::Peekable::peek_mut")
methods to look at the next element of the iterator without consuming
it. See their documentation for more information. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.peekable)

</div>

<div id="method.skip_while" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#1121-1124"
class="src">Source</a></span><a href="#method.skip_while" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.skip_while"
class="fn">skip_while</a>\<P\>(self, predicate: P) -\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/adapters/skip_while/struct.SkipWhile.html"
class="struct"
title="struct core::iter::adapters::skip_while::SkipWhile">SkipWhile</a>\<Self, P\>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, P: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(&Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>) -\>
<a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>,

</div>

</div>

<div class="docblock">

Creates an iterator that
[`skip`](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.skip "method core::iter::traits::iterator::Iterator::skip")s
elements based on a predicate. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.skip_while)

</div>

<div id="method.take_while" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#1199-1202"
class="src">Source</a></span><a href="#method.take_while" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.take_while"
class="fn">take_while</a>\<P\>(self, predicate: P) -\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/adapters/take_while/struct.TakeWhile.html"
class="struct"
title="struct core::iter::adapters::take_while::TakeWhile">TakeWhile</a>\<Self, P\>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, P: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(&Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>) -\>
<a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>,

</div>

</div>

<div class="docblock">

Creates an iterator that yields elements based on a predicate. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.take_while)

</div>

<div id="method.map_while" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.57.0">1.57.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#1287-1290"
class="src">Source</a></span><a href="#method.map_while" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.map_while"
class="fn">map_while</a>\<B, P\>(self, predicate: P) -\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/adapters/map_while/struct.MapWhile.html"
class="struct"
title="struct core::iter::adapters::map_while::MapWhile">MapWhile</a>\<Self, P\>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, P: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>) -\>
<a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<B\>,

</div>

</div>

<div class="docblock">

Creates an iterator that both yields elements based on a predicate and
maps. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.map_while)

</div>

<div id="method.skip" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#1316-1318"
class="src">Source</a></span><a href="#method.skip" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.skip"
class="fn">skip</a>(self, n: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>) -\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/adapters/skip/struct.Skip.html"
class="struct" title="struct core::iter::adapters::skip::Skip">Skip</a>\<Self\>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Creates an iterator that skips the first `n` elements. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.skip)

</div>

<div id="method.take" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#1388-1390"
class="src">Source</a></span><a href="#method.take" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.take"
class="fn">take</a>(self, n: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>) -\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/adapters/take/struct.Take.html"
class="struct" title="struct core::iter::adapters::take::Take">Take</a>\<Self\>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Creates an iterator that yields the first `n` elements, or fewer if the
underlying iterator ends sooner. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.take)

</div>

<div id="method.scan" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#1435-1438"
class="src">Source</a></span><a href="#method.scan" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.scan"
class="fn">scan</a>\<St, B, F\>(self, initial_state: St, f: F) -\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/adapters/scan/struct.Scan.html"
class="struct" title="struct core::iter::adapters::scan::Scan">Scan</a>\<Self, St, F\>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;mut St</a>, Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>) -\>
<a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<B\>,

</div>

</div>

<div class="docblock">

An iterator adapter which, like
[`fold`](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.fold "method core::iter::traits::iterator::Iterator::fold"),
holds internal state, but unlike
[`fold`](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.fold "method core::iter::traits::iterator::Iterator::fold"),
produces a new iterator. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.scan)

</div>

<div id="method.flat_map" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#1473-1477"
class="src">Source</a></span><a href="#method.flat_map" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.flat_map"
class="fn">flat_map</a>\<U, F\>(self, f: F) -\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/adapters/flatten/struct.FlatMap.html"
class="struct"
title="struct core::iter::adapters::flatten::FlatMap">FlatMap</a>\<Self, U, F\>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, U: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>,
F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>) -\>
U,

</div>

</div>

<div class="docblock">

Creates an iterator that works like map, but flattens nested structure.
[Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.flat_map)

</div>

<div id="method.flatten" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.29.0">1.29.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#1557-1560"
class="src">Source</a></span><a href="#method.flatten" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.flatten"
class="fn">flatten</a>(self) -\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/adapters/flatten/struct.Flatten.html"
class="struct"
title="struct core::iter::adapters::flatten::Flatten">Flatten</a>\<Self\>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>,

</div>

</div>

<div class="docblock">

Creates an iterator that flattens nested structure. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.flatten)

</div>

<div id="method.map_windows" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#1713-1716"
class="src rightside">Source</a><a href="#method.map_windows" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.map_windows"
class="fn">map_windows</a>\<F, R, const N: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>\>(self, f: F) -\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/adapters/map_windows/struct.MapWindows.html"
class="struct"
title="struct core::iter::adapters::map_windows::MapWindows">MapWindows</a>\<Self, F, N\>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(&\[Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>;
<a href="https://doc.rust-lang.org/1.92.0/core/primitive.array.html"
class="primitive">N</a>\]) -\> R,

</div>

</div>

<span class="item-info"></span>

<div class="stab unstable">

🔬This is a nightly-only experimental API. (`iter_map_windows`)

</div>

<div class="docblock">

Calls the given function `f` for each contiguous window of size `N` over
`self` and returns an iterator over the outputs of `f`. Like
[`slice::windows()`](https://doc.rust-lang.org/1.92.0/core/primitive.slice.html#method.windows "method slice::windows"),
the windows during mapping overlap as well. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.map_windows)

</div>

<div id="method.fuse" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#1775-1777"
class="src">Source</a></span><a href="#method.fuse" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.fuse"
class="fn">fuse</a>(self) -\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/adapters/fuse/struct.Fuse.html"
class="struct" title="struct core::iter::adapters::fuse::Fuse">Fuse</a>\<Self\>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Creates an iterator which ends after the first
[`None`](https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html#variant.None "variant core::option::Option::None").
[Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.fuse)

</div>

<div id="method.inspect" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#1859-1862"
class="src">Source</a></span><a href="#method.inspect" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.inspect"
class="fn">inspect</a>\<F\>(self, f: F) -\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/adapters/inspect/struct.Inspect.html"
class="struct"
title="struct core::iter::adapters::inspect::Inspect">Inspect</a>\<Self, F\>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(&Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>),

</div>

</div>

<div class="docblock">

Does something with each element of an iterator, passing the value on.
[Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.inspect)

</div>

<div id="method.by_ref" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#1896-1898"
class="src">Source</a></span><a href="#method.by_ref" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.by_ref"
class="fn">by_ref</a>(&mut self) -\> &mut Self

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Creates a “by reference” adapter for this instance of `Iterator`. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.by_ref)

</div>

<div id="method.collect" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#2015-2017"
class="src">Source</a></span><a href="#method.collect" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.collect"
class="fn">collect</a>\<B\>(self) -\> B

<div class="where">

where B: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.FromIterator.html"
class="trait"
title="trait core::iter::traits::collect::FromIterator">FromIterator</a>\<Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>\>,
Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Transforms an iterator into a collection. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.collect)

</div>

<div id="method.try_collect" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#2102-2106"
class="src rightside">Source</a><a href="#method.try_collect" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.try_collect"
class="fn">try_collect</a>\<B\>( &mut self, ) -\> \<\<Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a> as <a
href="https://doc.rust-lang.org/1.92.0/core/ops/try_trait/trait.Try.html"
class="trait" title="trait core::ops::try_trait::Try">Try</a>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/ops/try_trait/trait.Try.html#associatedtype.Residual"
class="associatedtype"
title="type core::ops::try_trait::Try::Residual">Residual</a> as <a
href="https://doc.rust-lang.org/1.92.0/core/ops/try_trait/trait.Residual.html"
class="trait" title="trait core::ops::try_trait::Residual">Residual</a>\<B\>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/ops/try_trait/trait.Residual.html#associatedtype.TryType"
class="associatedtype"
title="type core::ops::try_trait::Residual::TryType">TryType</a>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/try_trait/trait.Try.html"
class="trait" title="trait core::ops::try_trait::Try">Try</a>,
\<Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a> as <a
href="https://doc.rust-lang.org/1.92.0/core/ops/try_trait/trait.Try.html"
class="trait" title="trait core::ops::try_trait::Try">Try</a>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/ops/try_trait/trait.Try.html#associatedtype.Residual"
class="associatedtype"
title="type core::ops::try_trait::Try::Residual">Residual</a>: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/try_trait/trait.Residual.html"
class="trait" title="trait core::ops::try_trait::Residual">Residual</a>\<B\>,
B: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.FromIterator.html"
class="trait"
title="trait core::iter::traits::collect::FromIterator">FromIterator</a>\<\<Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a> as <a
href="https://doc.rust-lang.org/1.92.0/core/ops/try_trait/trait.Try.html"
class="trait" title="trait core::ops::try_trait::Try">Try</a>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/ops/try_trait/trait.Try.html#associatedtype.Output"
class="associatedtype"
title="type core::ops::try_trait::Try::Output">Output</a>\>,

</div>

</div>

<span class="item-info"></span>

<div class="stab unstable">

🔬This is a nightly-only experimental API. (`iterator_try_collect`)

</div>

<div class="docblock">

Fallibly transforms an iterator into a collection, short circuiting if a
failure is encountered. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.try_collect)

</div>

<div id="method.collect_into" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#2174-2176"
class="src rightside">Source</a><a href="#method.collect_into" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.collect_into"
class="fn">collect_into</a>\<E\>(self, collection: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;mut E</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;mut E</a>

<div class="where">

where E: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html"
class="trait"
title="trait core::iter::traits::collect::Extend">Extend</a>\<Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>\>,
Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<span class="item-info"></span>

<div class="stab unstable">

🔬This is a nightly-only experimental API. (`iter_collect_into`)

</div>

<div class="docblock">

Collects all the items from an iterator into a collection. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.collect_into)

</div>

<div id="method.partition" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#2206-2210"
class="src">Source</a></span><a href="#method.partition" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.partition"
class="fn">partition</a>\<B, F\>(self, f: F) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.tuple.html"
class="primitive">(B, B)</a>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, B: <a
href="https://doc.rust-lang.org/1.92.0/core/default/trait.Default.html"
class="trait" title="trait core::default::Default">Default</a> + <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html"
class="trait"
title="trait core::iter::traits::collect::Extend">Extend</a>\<Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>\>, F:
<a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(&Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>) -\>
<a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>,

</div>

</div>

<div class="docblock">

Consumes an iterator, creating two collections from it. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.partition)

</div>

<div id="method.is_partitioned" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#2325-2328"
class="src rightside">Source</a><a href="#method.is_partitioned" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.is_partitioned"
class="fn">is_partitioned</a>\<P\>(self, predicate: P) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, P: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>) -\>
<a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>,

</div>

</div>

<span class="item-info"></span>

<div class="stab unstable">

🔬This is a nightly-only experimental API. (`iter_is_partitioned`)

</div>

<div class="docblock">

Checks if the elements of this iterator are partitioned according to the
given predicate, such that all those that return `true` precede all
those that return `false`. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.is_partitioned)

</div>

<div id="method.try_fold" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.27.0">1.27.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#2419-2423"
class="src">Source</a></span><a href="#method.try_fold" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.try_fold"
class="fn">try_fold</a>\<B, F, R\>(&mut self, init: B, f: F) -\> R

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(B,
Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>) -\>
R, R: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/try_trait/trait.Try.html"
class="trait" title="trait core::ops::try_trait::Try">Try</a>\<Output =
B\>,

</div>

</div>

<div class="docblock">

An iterator method that applies a function as long as it returns
successfully, producing a single, final value. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.try_fold)

</div>

<div id="method.try_for_each" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.27.0">1.27.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#2477-2481"
class="src">Source</a></span><a href="#method.try_for_each" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.try_for_each"
class="fn">try_for_each</a>\<F, R\>(&mut self, f: F) -\> R

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>) -\>
R, R: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/try_trait/trait.Try.html"
class="trait" title="trait core::ops::try_trait::Try">Try</a>\<Output =
<a href="https://doc.rust-lang.org/1.92.0/core/primitive.unit.html"
class="primitive">()</a>\>,

</div>

</div>

<div class="docblock">

An iterator method that applies a fallible function to each item in the
iterator, stopping at the first error and returning that error. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.try_for_each)

</div>

<div id="method.fold" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#2596-2599"
class="src">Source</a></span><a href="#method.fold" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.fold"
class="fn">fold</a>\<B, F\>(self, init: B, f: F) -\> B

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(B,
Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>) -\>
B,

</div>

</div>

<div class="docblock">

Folds every element into an accumulator by applying an operation,
returning the final result. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.fold)

</div>

<div id="method.reduce" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.51.0">1.51.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#2633-2636"
class="src">Source</a></span><a href="#method.reduce" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.reduce"
class="fn">reduce</a>\<F\>(self, f: F) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>\>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>,
Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>) -\>
Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>,

</div>

</div>

<div class="docblock">

Reduces the elements to a single one, by repeatedly applying a reducing
operation. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.reduce)

</div>

<div id="method.try_reduce" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#2704-2710"
class="src rightside">Source</a><a href="#method.try_reduce" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.try_reduce"
class="fn">try_reduce</a>\<R\>( &mut self, f: impl <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>, Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>) -\> R, ) -\> \<\<R as <a
href="https://doc.rust-lang.org/1.92.0/core/ops/try_trait/trait.Try.html"
class="trait" title="trait core::ops::try_trait::Try">Try</a>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/ops/try_trait/trait.Try.html#associatedtype.Residual"
class="associatedtype"
title="type core::ops::try_trait::Try::Residual">Residual</a> as <a
href="https://doc.rust-lang.org/1.92.0/core/ops/try_trait/trait.Residual.html"
class="trait" title="trait core::ops::try_trait::Residual">Residual</a>\<<a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<\<R as <a
href="https://doc.rust-lang.org/1.92.0/core/ops/try_trait/trait.Try.html"
class="trait" title="trait core::ops::try_trait::Try">Try</a>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/ops/try_trait/trait.Try.html#associatedtype.Output"
class="associatedtype"
title="type core::ops::try_trait::Try::Output">Output</a>\>\>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/ops/try_trait/trait.Residual.html#associatedtype.TryType"
class="associatedtype"
title="type core::ops::try_trait::Residual::TryType">TryType</a>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, R: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/try_trait/trait.Try.html"
class="trait" title="trait core::ops::try_trait::Try">Try</a>\<Output =
Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>\>,
\<R as <a
href="https://doc.rust-lang.org/1.92.0/core/ops/try_trait/trait.Try.html"
class="trait" title="trait core::ops::try_trait::Try">Try</a>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/ops/try_trait/trait.Try.html#associatedtype.Residual"
class="associatedtype"
title="type core::ops::try_trait::Try::Residual">Residual</a>: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/try_trait/trait.Residual.html"
class="trait" title="trait core::ops::try_trait::Residual">Residual</a>\<<a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>\>\>,

</div>

</div>

<span class="item-info"></span>

<div class="stab unstable">

🔬This is a nightly-only experimental API. (`iterator_try_reduce`)

</div>

<div class="docblock">

Reduces the elements to a single one by repeatedly applying a reducing
operation. If the closure returns a failure, the failure is propagated
back to the caller immediately. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.try_reduce)

</div>

<div id="method.all" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#2762-2765"
class="src">Source</a></span><a href="#method.all" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.all"
class="fn">all</a>\<F\>(&mut self, f: F) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>) -\>
<a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>,

</div>

</div>

<div class="docblock">

Tests if every element of the iterator matches a predicate. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.all)

</div>

<div id="method.any" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#2815-2818"
class="src">Source</a></span><a href="#method.any" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.any"
class="fn">any</a>\<F\>(&mut self, f: F) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>) -\>
<a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>,

</div>

</div>

<div class="docblock">

Tests if any element of the iterator matches a predicate. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.any)

</div>

<div id="method.find" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#2877-2880"
class="src">Source</a></span><a href="#method.find" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.find"
class="fn">find</a>\<P\>(&mut self, predicate: P) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>\>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, P: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(&Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>) -\>
<a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>,

</div>

</div>

<div class="docblock">

Searches for an element of an iterator that satisfies a predicate. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.find)

</div>

<div id="method.find_map" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.30.0">1.30.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#2908-2911"
class="src">Source</a></span><a href="#method.find_map" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.find_map"
class="fn">find_map</a>\<B, F\>(&mut self, f: F) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<B\>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>) -\>
<a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<B\>,

</div>

</div>

<div class="docblock">

Applies function to the elements of iterator and returns the first
non-none result. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.find_map)

</div>

<div id="method.try_find" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#2966-2972"
class="src rightside">Source</a><a href="#method.try_find" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.try_find"
class="fn">try_find</a>\<R\>( &mut self, f: impl <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(&Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>) -\> R, ) -\> \<\<R as <a
href="https://doc.rust-lang.org/1.92.0/core/ops/try_trait/trait.Try.html"
class="trait" title="trait core::ops::try_trait::Try">Try</a>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/ops/try_trait/trait.Try.html#associatedtype.Residual"
class="associatedtype"
title="type core::ops::try_trait::Try::Residual">Residual</a> as <a
href="https://doc.rust-lang.org/1.92.0/core/ops/try_trait/trait.Residual.html"
class="trait" title="trait core::ops::try_trait::Residual">Residual</a>\<<a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>\>\>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/ops/try_trait/trait.Residual.html#associatedtype.TryType"
class="associatedtype"
title="type core::ops::try_trait::Residual::TryType">TryType</a>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, R: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/try_trait/trait.Try.html"
class="trait" title="trait core::ops::try_trait::Try">Try</a>\<Output =
<a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>\>, \<R as <a
href="https://doc.rust-lang.org/1.92.0/core/ops/try_trait/trait.Try.html"
class="trait" title="trait core::ops::try_trait::Try">Try</a>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/ops/try_trait/trait.Try.html#associatedtype.Residual"
class="associatedtype"
title="type core::ops::try_trait::Try::Residual">Residual</a>: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/try_trait/trait.Residual.html"
class="trait" title="trait core::ops::try_trait::Residual">Residual</a>\<<a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>\>\>,

</div>

</div>

<span class="item-info"></span>

<div class="stab unstable">

🔬This is a nightly-only experimental API. (`try_find`)

</div>

<div class="docblock">

Applies function to the elements of iterator and returns the first true
result or the first error. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.try_find)

</div>

<div id="method.position" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#3049-3052"
class="src">Source</a></span><a href="#method.position" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.position"
class="fn">position</a>\<P\>(&mut self, predicate: P) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>\>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, P: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>) -\>
<a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>,

</div>

</div>

<div class="docblock">

Searches for an element in an iterator, returning its index. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.position)

</div>

<div id="method.max" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#3163-3166"
class="src">Source</a></span><a href="#method.max" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.max"
class="fn">max</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>\>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Ord.html"
class="trait" title="trait core::cmp::Ord">Ord</a>,

</div>

</div>

<div class="docblock">

Returns the maximum element of an iterator. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.max)

</div>

<div id="method.min" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#3199-3202"
class="src">Source</a></span><a href="#method.min" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.min"
class="fn">min</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>\>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Ord.html"
class="trait" title="trait core::cmp::Ord">Ord</a>,

</div>

</div>

<div class="docblock">

Returns the minimum element of an iterator. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.min)

</div>

<div id="method.max_by_key" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.6.0">1.6.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#3221-3224"
class="src">Source</a></span><a href="#method.max_by_key" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.max_by_key"
class="fn">max_by_key</a>\<B, F\>(self, f: F) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>\>

<div class="where">

where B:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Ord.html"
class="trait" title="trait core::cmp::Ord">Ord</a>, Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(&Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>) -\>
B,

</div>

</div>

<div class="docblock">

Returns the element that gives the maximum value from the specified
function. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.max_by_key)

</div>

<div id="method.max_by" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.15.0">1.15.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#3254-3257"
class="src">Source</a></span><a href="#method.max_by" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.max_by"
class="fn">max_by</a>\<F\>(self, compare: F) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>\>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(&Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>,
&Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>) -\>
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/enum.Ordering.html"
class="enum" title="enum core::cmp::Ordering">Ordering</a>,

</div>

</div>

<div class="docblock">

Returns the element that gives the maximum value with respect to the
specified comparison function. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.max_by)

</div>

<div id="method.min_by_key" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.6.0">1.6.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#3281-3284"
class="src">Source</a></span><a href="#method.min_by_key" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.min_by_key"
class="fn">min_by_key</a>\<B, F\>(self, f: F) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>\>

<div class="where">

where B:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Ord.html"
class="trait" title="trait core::cmp::Ord">Ord</a>, Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(&Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>) -\>
B,

</div>

</div>

<div class="docblock">

Returns the element that gives the minimum value from the specified
function. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.min_by_key)

</div>

<div id="method.min_by" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.15.0">1.15.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#3314-3317"
class="src">Source</a></span><a href="#method.min_by" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.min_by"
class="fn">min_by</a>\<F\>(self, compare: F) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>\>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(&Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>,
&Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>) -\>
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/enum.Ordering.html"
class="enum" title="enum core::cmp::Ordering">Ordering</a>,

</div>

</div>

<div class="docblock">

Returns the element that gives the minimum value with respect to the
specified comparison function. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.min_by)

</div>

<div id="method.unzip" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#3387-3391"
class="src">Source</a></span><a href="#method.unzip" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.unzip"
class="fn">unzip</a>\<A, B, FromA, FromB\>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.tuple.html"
class="primitive">(FromA, FromB)</a>

<div class="where">

where FromA: <a
href="https://doc.rust-lang.org/1.92.0/core/default/trait.Default.html"
class="trait" title="trait core::default::Default">Default</a> + <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html"
class="trait"
title="trait core::iter::traits::collect::Extend">Extend</a>\<A\>,
FromB: <a
href="https://doc.rust-lang.org/1.92.0/core/default/trait.Default.html"
class="trait" title="trait core::default::Default">Default</a> + <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html"
class="trait"
title="trait core::iter::traits::collect::Extend">Extend</a>\<B\>, Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a> + <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html"
class="trait"
title="trait core::iter::traits::iterator::Iterator">Iterator</a>\<Item
= <a href="https://doc.rust-lang.org/1.92.0/core/primitive.tuple.html"
class="primitive">(A, B)</a>\>,

</div>

</div>

<div class="docblock">

Converts an iterator of pairs into a pair of containers. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.unzip)

</div>

<div id="method.copied" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.36.0">1.36.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#3418-3421"
class="src">Source</a></span><a href="#method.copied" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.copied"
class="fn">copied</a>\<'a, T\>(self) -\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/adapters/copied/struct.Copied.html"
class="struct"
title="struct core::iter::adapters::copied::Copied">Copied</a>\<Self\>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Copy.html"
class="trait" title="trait core::marker::Copy">Copy</a> + 'a, Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a> + <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html"
class="trait"
title="trait core::iter::traits::iterator::Iterator">Iterator</a>\<Item
=
<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;'a T</a>\>,

</div>

</div>

<div class="docblock">

Creates an iterator which copies all of its elements. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.copied)

</div>

<div id="method.cloned" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#3466-3469"
class="src">Source</a></span><a href="#method.cloned" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.cloned"
class="fn">cloned</a>\<'a, T\>(self) -\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/adapters/cloned/struct.Cloned.html"
class="struct"
title="struct core::iter::adapters::cloned::Cloned">Cloned</a>\<Self\>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a> + 'a, Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a> + <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html"
class="trait"
title="trait core::iter::traits::iterator::Iterator">Iterator</a>\<Item
=
<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;'a T</a>\>,

</div>

</div>

<div class="docblock">

Creates an iterator which
[`clone`](https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html#tymethod.clone "method core::clone::Clone::clone")s
all of its elements. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.cloned)

</div>

<div id="method.array_chunks" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#3540-3542"
class="src rightside">Source</a><a href="#method.array_chunks" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.array_chunks"
class="fn">array_chunks</a>\<const N: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>\>(self) -\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/adapters/array_chunks/struct.ArrayChunks.html"
class="struct"
title="struct core::iter::adapters::array_chunks::ArrayChunks">ArrayChunks</a>\<Self, N\>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<span class="item-info"></span>

<div class="stab unstable">

🔬This is a nightly-only experimental API. (`iter_array_chunks`)

</div>

<div class="docblock">

Returns an iterator over `N` elements of the iterator at a time. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.array_chunks)

</div>

<div id="method.sum" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.11.0">1.11.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#3576-3579"
class="src">Source</a></span><a href="#method.sum" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.sum"
class="fn">sum</a>\<S\>(self) -\> S

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, S: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/accum/trait.Sum.html"
class="trait" title="trait core::iter::traits::accum::Sum">Sum</a>\<Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>\>,

</div>

</div>

<div class="docblock">

Sums the elements of an iterator. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.sum)

</div>

<div id="method.product" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.11.0">1.11.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#3608-3611"
class="src">Source</a></span><a href="#method.product" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.product"
class="fn">product</a>\<P\>(self) -\> P

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, P: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/accum/trait.Product.html"
class="trait"
title="trait core::iter::traits::accum::Product">Product</a>\<Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>\>,

</div>

</div>

<div class="docblock">

Iterates over the entire iterator, multiplying all the elements [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.product)

</div>

<div id="method.cmp" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.5.0">1.5.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#3629-3633"
class="src">Source</a></span><a href="#method.cmp" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.cmp"
class="fn">cmp</a>\<I\>(self, other: I) -\> <a href="https://doc.rust-lang.org/1.92.0/core/cmp/enum.Ordering.html"
class="enum" title="enum core::cmp::Ordering">Ordering</a>

<div class="where">

where I: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>\<Item
= Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>\>,
Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Ord.html"
class="trait" title="trait core::cmp::Ord">Ord</a>, Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

[Lexicographically](https://doc.rust-lang.org/1.92.0/core/cmp/trait.Ord.html#lexicographical-comparison "trait core::cmp::Ord")
compares the elements of this
[`Iterator`](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html "trait core::iter::traits::iterator::Iterator")
with those of another. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.cmp)

</div>

<div id="method.cmp_by" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#3656-3660"
class="src rightside">Source</a><a href="#method.cmp_by" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.cmp_by"
class="fn">cmp_by</a>\<I, F\>(self, other: I, cmp: F) -\> <a href="https://doc.rust-lang.org/1.92.0/core/cmp/enum.Ordering.html"
class="enum" title="enum core::cmp::Ordering">Ordering</a>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, I: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>,
F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>, \<I
as <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::collect::IntoIterator::Item">Item</a>)
-\>
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/enum.Ordering.html"
class="enum" title="enum core::cmp::Ordering">Ordering</a>,

</div>

</div>

<span class="item-info"></span>

<div class="stab unstable">

🔬This is a nightly-only experimental API. (`iter_order_by`)

</div>

<div class="docblock">

[Lexicographically](https://doc.rust-lang.org/1.92.0/core/cmp/trait.Ord.html#lexicographical-comparison "trait core::cmp::Ord")
compares the elements of this
[`Iterator`](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html "trait core::iter::traits::iterator::Iterator")
with those of another with respect to the specified comparison function.
[Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.cmp_by)

</div>

<div id="method.partial_cmp" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.5.0">1.5.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#3712-3716"
class="src">Source</a></span><a href="#method.partial_cmp" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.partial_cmp"
class="fn">partial_cmp</a>\<I\>(self, other: I) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="https://doc.rust-lang.org/1.92.0/core/cmp/enum.Ordering.html"
class="enum" title="enum core::cmp::Ordering">Ordering</a>\>

<div class="where">

where I: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>,
Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>: <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialOrd.html"
class="trait" title="trait core::cmp::PartialOrd">PartialOrd</a>\<\<I as
<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::collect::IntoIterator::Item">Item</a>\>,
Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

[Lexicographically](https://doc.rust-lang.org/1.92.0/core/cmp/trait.Ord.html#lexicographical-comparison "trait core::cmp::Ord")
compares the
[`PartialOrd`](https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialOrd.html "trait core::cmp::PartialOrd")
elements of this
[`Iterator`](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html "trait core::iter::traits::iterator::Iterator")
with those of another. The comparison works like short-circuit
evaluation, returning a result without comparing the remaining elements.
As soon as an order can be determined, the evaluation stops and a result
is returned. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.partial_cmp)

</div>

<div id="method.partial_cmp_by" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#3748-3752"
class="src rightside">Source</a><a href="#method.partial_cmp_by" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.partial_cmp_by"
class="fn">partial_cmp_by</a>\<I, F\>(self, other: I, partial_cmp: F) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="https://doc.rust-lang.org/1.92.0/core/cmp/enum.Ordering.html"
class="enum" title="enum core::cmp::Ordering">Ordering</a>\>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, I: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>,
F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>, \<I
as <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::collect::IntoIterator::Item">Item</a>)
-\>
<a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="https://doc.rust-lang.org/1.92.0/core/cmp/enum.Ordering.html"
class="enum" title="enum core::cmp::Ordering">Ordering</a>\>,

</div>

</div>

<span class="item-info"></span>

<div class="stab unstable">

🔬This is a nightly-only experimental API. (`iter_order_by`)

</div>

<div class="docblock">

[Lexicographically](https://doc.rust-lang.org/1.92.0/core/cmp/trait.Ord.html#lexicographical-comparison "trait core::cmp::Ord")
compares the elements of this
[`Iterator`](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html "trait core::iter::traits::iterator::Iterator")
with those of another with respect to the specified comparison function.
[Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.partial_cmp_by)

</div>

<div id="method.eq" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.5.0">1.5.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#3781-3785"
class="src">Source</a></span><a href="#method.eq" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.eq"
class="fn">eq</a>\<I\>(self, other: I) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>

<div class="where">

where I: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>,
Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialEq.html"
class="trait" title="trait core::cmp::PartialEq">PartialEq</a>\<\<I as
<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::collect::IntoIterator::Item">Item</a>\>,
Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Determines if the elements of this
[`Iterator`](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html "trait core::iter::traits::iterator::Iterator")
are equal to those of another. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.eq)

</div>

<div id="method.eq_by" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#3804-3808"
class="src rightside">Source</a><a href="#method.eq_by" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.eq_by"
class="fn">eq_by</a>\<I, F\>(self, other: I, eq: F) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, I: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>,
F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>, \<I
as <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::collect::IntoIterator::Item">Item</a>)
-\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>,

</div>

</div>

<span class="item-info"></span>

<div class="stab unstable">

🔬This is a nightly-only experimental API. (`iter_order_by`)

</div>

<div class="docblock">

Determines if the elements of this
[`Iterator`](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html "trait core::iter::traits::iterator::Iterator")
are equal to those of another with respect to the specified equality
function. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.eq_by)

</div>

<div id="method.ne" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.5.0">1.5.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#3833-3837"
class="src">Source</a></span><a href="#method.ne" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.ne"
class="fn">ne</a>\<I\>(self, other: I) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>

<div class="where">

where I: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>,
Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialEq.html"
class="trait" title="trait core::cmp::PartialEq">PartialEq</a>\<\<I as
<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::collect::IntoIterator::Item">Item</a>\>,
Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Determines if the elements of this
[`Iterator`](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html "trait core::iter::traits::iterator::Iterator")
are not equal to those of another. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.ne)

</div>

<div id="method.lt" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.5.0">1.5.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#3854-3858"
class="src">Source</a></span><a href="#method.lt" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.lt"
class="fn">lt</a>\<I\>(self, other: I) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>

<div class="where">

where I: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>,
Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>: <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialOrd.html"
class="trait" title="trait core::cmp::PartialOrd">PartialOrd</a>\<\<I as
<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::collect::IntoIterator::Item">Item</a>\>,
Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Determines if the elements of this
[`Iterator`](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html "trait core::iter::traits::iterator::Iterator")
are
[lexicographically](https://doc.rust-lang.org/1.92.0/core/cmp/trait.Ord.html#lexicographical-comparison "trait core::cmp::Ord")
less than those of another. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.lt)

</div>

<div id="method.le" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.5.0">1.5.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#3875-3879"
class="src">Source</a></span><a href="#method.le" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.le"
class="fn">le</a>\<I\>(self, other: I) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>

<div class="where">

where I: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>,
Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>: <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialOrd.html"
class="trait" title="trait core::cmp::PartialOrd">PartialOrd</a>\<\<I as
<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::collect::IntoIterator::Item">Item</a>\>,
Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Determines if the elements of this
[`Iterator`](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html "trait core::iter::traits::iterator::Iterator")
are
[lexicographically](https://doc.rust-lang.org/1.92.0/core/cmp/trait.Ord.html#lexicographical-comparison "trait core::cmp::Ord")
less or equal to those of another. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.le)

</div>

<div id="method.gt" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.5.0">1.5.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#3896-3900"
class="src">Source</a></span><a href="#method.gt" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.gt"
class="fn">gt</a>\<I\>(self, other: I) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>

<div class="where">

where I: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>,
Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>: <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialOrd.html"
class="trait" title="trait core::cmp::PartialOrd">PartialOrd</a>\<\<I as
<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::collect::IntoIterator::Item">Item</a>\>,
Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Determines if the elements of this
[`Iterator`](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html "trait core::iter::traits::iterator::Iterator")
are
[lexicographically](https://doc.rust-lang.org/1.92.0/core/cmp/trait.Ord.html#lexicographical-comparison "trait core::cmp::Ord")
greater than those of another. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.gt)

</div>

<div id="method.ge" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.5.0">1.5.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#3917-3921"
class="src">Source</a></span><a href="#method.ge" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.ge"
class="fn">ge</a>\<I\>(self, other: I) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>

<div class="where">

where I: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>,
Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>: <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialOrd.html"
class="trait" title="trait core::cmp::PartialOrd">PartialOrd</a>\<\<I as
<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::collect::IntoIterator::Item">Item</a>\>,
Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Determines if the elements of this
[`Iterator`](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html "trait core::iter::traits::iterator::Iterator")
are
[lexicographically](https://doc.rust-lang.org/1.92.0/core/cmp/trait.Ord.html#lexicographical-comparison "trait core::cmp::Ord")
greater than or equal to those of another. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.ge)

</div>

<div id="method.is_sorted" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.82.0">1.82.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#3946-3949"
class="src">Source</a></span><a href="#method.is_sorted" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.is_sorted"
class="fn">is_sorted</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>: <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialOrd.html"
class="trait" title="trait core::cmp::PartialOrd">PartialOrd</a>,

</div>

</div>

<div class="docblock">

Checks if the elements of this iterator are sorted. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.is_sorted)

</div>

<div id="method.is_sorted_by" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.82.0">1.82.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#3972-3975"
class="src">Source</a></span><a href="#method.is_sorted_by" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.is_sorted_by"
class="fn">is_sorted_by</a>\<F\>(self, compare: F) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(&Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>,
&Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>) -\>
<a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>,

</div>

</div>

<div class="docblock">

Checks if the elements of this iterator are sorted using the given
comparator function. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.is_sorted_by)

</div>

<div id="method.is_sorted_by_key" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.82.0">1.82.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/iterator.rs.html#4016-4020"
class="src">Source</a></span><a href="#method.is_sorted_by_key" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.is_sorted_by_key"
class="fn">is_sorted_by_key</a>\<F, K\>(self, f: F) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>) -\>
K, K: <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialOrd.html"
class="trait" title="trait core::cmp::PartialOrd">PartialOrd</a>,

</div>

</div>

<div class="docblock">

Checks if the elements of this iterator are sorted using the given key
extraction function. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#method.is_sorted_by_key)

</div>

</div>

<div id="impl-FusedIterator-for-IntoIter%3CK,+V,+A%3E"
class="section impl">

<a href="../../src/hashbrown/map.rs.html#4752"
class="src rightside">Source</a><a href="#impl-FusedIterator-for-IntoIter%3CK,+V,+A%3E"
class="anchor">§</a>

### impl\<K, V, A: Allocator + <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/marker/trait.FusedIterator.html"
class="trait"
title="trait core::iter::traits::marker::FusedIterator">FusedIterator</a> for <a href="struct.IntoIter.html" class="struct"
title="struct hashbrown::hash_map::IntoIter">IntoIter</a>\<K, V, A\>

</div>

</div>

## Auto Trait Implementations<a href="#synthetic-implementations" class="anchor">§</a>

<div id="synthetic-implementations-list">

<div id="impl-Freeze-for-IntoIter%3CK,+V,+A%3E" class="section impl">

<a href="#impl-Freeze-for-IntoIter%3CK,+V,+A%3E" class="anchor">§</a>

### impl\<K, V, A\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a> for <a href="struct.IntoIter.html" class="struct"
title="struct hashbrown::hash_map::IntoIter">IntoIter</a>\<K, V, A\>

<div class="where">

where A:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a>,

</div>

</div>

<div id="impl-RefUnwindSafe-for-IntoIter%3CK,+V,+A%3E"
class="section impl">

<a href="#impl-RefUnwindSafe-for-IntoIter%3CK,+V,+A%3E"
class="anchor">§</a>

### impl\<K, V, A\> <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a> for <a href="struct.IntoIter.html" class="struct"
title="struct hashbrown::hash_map::IntoIter">IntoIter</a>\<K, V, A\>

<div class="where">

where A: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a>,
K: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a>,
V: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a>,

</div>

</div>

<div id="impl-Send-for-IntoIter%3CK,+V,+A%3E" class="section impl">

<a href="#impl-Send-for-IntoIter%3CK,+V,+A%3E" class="anchor">§</a>

### impl\<K, V, A\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a> for <a href="struct.IntoIter.html" class="struct"
title="struct hashbrown::hash_map::IntoIter">IntoIter</a>\<K, V, A\>

<div class="where">

where A:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a>, K:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a>, V:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a>,

</div>

</div>

<div id="impl-Sync-for-IntoIter%3CK,+V,+A%3E" class="section impl">

<a href="#impl-Sync-for-IntoIter%3CK,+V,+A%3E" class="anchor">§</a>

### impl\<K, V, A\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a> for <a href="struct.IntoIter.html" class="struct"
title="struct hashbrown::hash_map::IntoIter">IntoIter</a>\<K, V, A\>

<div class="where">

where A:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a>, K:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a>, V:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a>,

</div>

</div>

<div id="impl-Unpin-for-IntoIter%3CK,+V,+A%3E" class="section impl">

<a href="#impl-Unpin-for-IntoIter%3CK,+V,+A%3E" class="anchor">§</a>

### impl\<K, V, A\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a> for <a href="struct.IntoIter.html" class="struct"
title="struct hashbrown::hash_map::IntoIter">IntoIter</a>\<K, V, A\>

<div class="where">

where A:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a>, K:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a>, V:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a>,

</div>

</div>

<div id="impl-UnwindSafe-for-IntoIter%3CK,+V,+A%3E"
class="section impl">

<a href="#impl-UnwindSafe-for-IntoIter%3CK,+V,+A%3E"
class="anchor">§</a>

### impl\<K, V, A\> <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a> for <a href="struct.IntoIter.html" class="struct"
title="struct hashbrown::hash_map::IntoIter">IntoIter</a>\<K, V, A\>

<div class="where">

where A: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a>, K: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a> + <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a>,
V: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a> + <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a>,

</div>

</div>

</div>

## Blanket Implementations<a href="#blanket-implementations" class="anchor">§</a>

<div id="blanket-implementations-list">

<div id="impl-Any-for-T" class="section impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/any.rs.html#138"
class="src rightside">Source</a><a href="#impl-Any-for-T" class="anchor">§</a>

### impl\<T\> <a href="https://doc.rust-lang.org/1.92.0/core/any/trait.Any.html"
class="trait" title="trait core::any::Any">Any</a> for T

<div class="where">

where T: 'static +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="impl-items">

<div id="method.type_id" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/any.rs.html#139"
class="src rightside">Source</a><a href="#method.type_id" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/any/trait.Any.html#tymethod.type_id"
class="fn">type_id</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/any/struct.TypeId.html"
class="struct" title="struct core::any::TypeId">TypeId</a>

</div>

<div class="docblock">

Gets the `TypeId` of `self`. [Read
more](https://doc.rust-lang.org/1.92.0/core/any/trait.Any.html#tymethod.type_id)

</div>

</div>

<div id="impl-Borrow%3CT%3E-for-T" class="section impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/borrow.rs.html#212"
class="src rightside">Source</a><a href="#impl-Borrow%3CT%3E-for-T" class="anchor">§</a>

### impl\<T\> <a href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.Borrow.html"
class="trait" title="trait core::borrow::Borrow">Borrow</a>\<T\> for T

<div class="where">

where T:
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="impl-items">

<div id="method.borrow" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/borrow.rs.html#214"
class="src rightside">Source</a><a href="#method.borrow" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.Borrow.html#tymethod.borrow"
class="fn">borrow</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;T</a>

</div>

<div class="docblock">

Immutably borrows from an owned value. [Read
more](https://doc.rust-lang.org/1.92.0/core/borrow/trait.Borrow.html#tymethod.borrow)

</div>

</div>

<div id="impl-BorrowMut%3CT%3E-for-T" class="section impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/borrow.rs.html#221"
class="src rightside">Source</a><a href="#impl-BorrowMut%3CT%3E-for-T" class="anchor">§</a>

### impl\<T\> <a
href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.BorrowMut.html"
class="trait" title="trait core::borrow::BorrowMut">BorrowMut</a>\<T\> for T

<div class="where">

where T:
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="impl-items">

<div id="method.borrow_mut" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/borrow.rs.html#222"
class="src rightside">Source</a><a href="#method.borrow_mut" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.BorrowMut.html#tymethod.borrow_mut"
class="fn">borrow_mut</a>(&mut self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;mut T</a>

</div>

<div class="docblock">

Mutably borrows from an owned value. [Read
more](https://doc.rust-lang.org/1.92.0/core/borrow/trait.BorrowMut.html#tymethod.borrow_mut)

</div>

</div>

<div id="impl-From%3CT%3E-for-T" class="section impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#785"
class="src rightside">Source</a><a href="#impl-From%3CT%3E-for-T" class="anchor">§</a>

### impl\<T\> <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<T\> for T

</div>

<div class="impl-items">

<div id="method.from" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#788"
class="src rightside">Source</a><a href="#method.from" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(t: T) -\> T

</div>

<div class="docblock">

Returns the argument unchanged.

</div>

</div>

<div id="impl-Into%3CU%3E-for-T" class="section impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#767-769"
class="src rightside">Source</a><a href="#impl-Into%3CU%3E-for-T" class="anchor">§</a>

### impl\<T, U\> <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.Into.html"
class="trait" title="trait core::convert::Into">Into</a>\<U\> for T

<div class="where">

where U:
<a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<T\>,

</div>

</div>

<div class="impl-items">

<div id="method.into" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#777"
class="src rightside">Source</a><a href="#method.into" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.Into.html#tymethod.into"
class="fn">into</a>(self) -\> U

</div>

<div class="docblock">

Calls `U::from(self)`.

That is, this conversion is whatever the implementation of
[`From`](https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html "trait core::convert::From")`<T> for U`
chooses to do.

</div>

</div>

<div id="impl-IntoIterator-for-I" class="section impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/collect.rs.html#314"
class="src rightside">Source</a><a href="#impl-IntoIterator-for-I" class="anchor">§</a>

### impl\<I\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a> for I

<div class="where">

where I: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html"
class="trait"
title="trait core::iter::traits::iterator::Iterator">Iterator</a>,

</div>

</div>

<div class="impl-items">

<div id="associatedtype.Item-1"
class="section associatedtype trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/collect.rs.html#315"
class="src rightside">Source</a><a href="#associatedtype.Item-1" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.Item"
class="associatedtype">Item</a> = \<I as <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html"
class="trait"
title="trait core::iter::traits::iterator::Iterator">Iterator</a>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/iterator/trait.Iterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::iterator::Iterator::Item">Item</a>

</div>

<div class="docblock">

The type of the elements being iterated over.

</div>

<div id="associatedtype.IntoIter"
class="section associatedtype trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/collect.rs.html#316"
class="src rightside">Source</a><a href="#associatedtype.IntoIter" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.IntoIter"
class="associatedtype">IntoIter</a> = I

</div>

<div class="docblock">

Which kind of iterator are we turning this into?

</div>

<div id="method.into_iter" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/collect.rs.html#319"
class="src rightside">Source</a><a href="#method.into_iter" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#tymethod.into_iter"
class="fn">into_iter</a>(self) -\> I

</div>

<div class="docblock">

Creates an iterator from a value. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#tymethod.into_iter)

</div>

</div>

<div id="impl-TryFrom%3CU%3E-for-T" class="section impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#827-829"
class="src rightside">Source</a><a href="#impl-TryFrom%3CU%3E-for-T" class="anchor">§</a>

### impl\<T, U\> <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html"
class="trait" title="trait core::convert::TryFrom">TryFrom</a>\<U\> for T

<div class="where">

where U:
<a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.Into.html"
class="trait" title="trait core::convert::Into">Into</a>\<T\>,

</div>

</div>

<div class="impl-items">

<div id="associatedtype.Error-1"
class="section associatedtype trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#831"
class="src rightside">Source</a><a href="#associatedtype.Error-1" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html#associatedtype.Error"
class="associatedtype">Error</a> = <a
href="https://doc.rust-lang.org/1.92.0/core/convert/enum.Infallible.html"
class="enum" title="enum core::convert::Infallible">Infallible</a>

</div>

<div class="docblock">

The type returned in the event of a conversion error.

</div>

<div id="method.try_from" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#834"
class="src rightside">Source</a><a href="#method.try_from" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html#tymethod.try_from"
class="fn">try_from</a>(value: U) -\> <a href="https://doc.rust-lang.org/1.92.0/core/result/enum.Result.html"
class="enum" title="enum core::result::Result">Result</a>\<T, \<T as <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html"
class="trait" title="trait core::convert::TryFrom">TryFrom</a>\<U\>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html#associatedtype.Error"
class="associatedtype"
title="type core::convert::TryFrom::Error">Error</a>\>

</div>

<div class="docblock">

Performs the conversion.

</div>

</div>

<div id="impl-TryInto%3CU%3E-for-T" class="section impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#811-813"
class="src rightside">Source</a><a href="#impl-TryInto%3CU%3E-for-T" class="anchor">§</a>

### impl\<T, U\> <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryInto.html"
class="trait" title="trait core::convert::TryInto">TryInto</a>\<U\> for T

<div class="where">

where U: <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html"
class="trait" title="trait core::convert::TryFrom">TryFrom</a>\<T\>,

</div>

</div>

<div class="impl-items">

<div id="associatedtype.Error"
class="section associatedtype trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#815"
class="src rightside">Source</a><a href="#associatedtype.Error" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryInto.html#associatedtype.Error"
class="associatedtype">Error</a> = \<U as <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html"
class="trait" title="trait core::convert::TryFrom">TryFrom</a>\<T\>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html#associatedtype.Error"
class="associatedtype"
title="type core::convert::TryFrom::Error">Error</a>

</div>

<div class="docblock">

The type returned in the event of a conversion error.

</div>

<div id="method.try_into" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#818"
class="src rightside">Source</a><a href="#method.try_into" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryInto.html#tymethod.try_into"
class="fn">try_into</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/result/enum.Result.html"
class="enum" title="enum core::result::Result">Result</a>\<U, \<U as <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html"
class="trait" title="trait core::convert::TryFrom">TryFrom</a>\<T\>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html#associatedtype.Error"
class="associatedtype"
title="type core::convert::TryFrom::Error">Error</a>\>

</div>

<div class="docblock">

Performs the conversion.

</div>

</div>

</div>

</div>

</div>
