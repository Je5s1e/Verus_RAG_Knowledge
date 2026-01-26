<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[indexmap](../index.html)::[map](index.html)

</div>

# Trait <span class="trait">MutableKeys</span> Copy item path

<span class="sub-heading"><a href="../../src/indexmap/mutable_keys.rs.html#19-46"
class="src">Source</a> </span>

</div>

``` rust
pub trait MutableKeys {
    type Key;
    type Value;

    // Required methods
    fn get_full_mut2<Q>(
        &mut self,
        key: &Q,
    ) -> Option<(usize, &mut Self::Key, &mut Self::Value)>
       where Q: Hash + Equivalent<Self::Key> + ?Sized;
    fn retain2<F>(&mut self, keep: F)
       where F: FnMut(&mut Self::Key, &mut Self::Value) -> bool;
    fn __private_marker(&self) -> PrivateMarker;
}
```

Expand description

<div class="docblock">

Opt-in mutable access to keys.

These methods expose `&mut K`, mutable references to the key as it is
stored in the map. You are allowed to modify the keys in the hashmap
**if the modification does not change the key’s hash and equality**.

If keys are modified erroneously, you can no longer look them up. This
is sound (memory safe) but a logical error hazard (just like
implementing PartialEq, Eq, or Hash incorrectly would be).

`use` this trait to enable its methods for `IndexMap`.

</div>

## Required Associated Types<a href="#required-associated-types" class="anchor">§</a>

<div class="methods">

<div id="associatedtype.Key" class="section method">

<a href="../../src/indexmap/mutable_keys.rs.html#20"
class="src rightside">Source</a>

#### type <a href="#associatedtype.Key" class="associatedtype">Key</a>

</div>

<div id="associatedtype.Value" class="section method">

<a href="../../src/indexmap/mutable_keys.rs.html#21"
class="src rightside">Source</a>

#### type <a href="#associatedtype.Value" class="associatedtype">Value</a>

</div>

</div>

## Required Methods<a href="#required-methods" class="anchor">§</a>

<div class="methods">

<div id="tymethod.get_full_mut2" class="section method">

<a href="../../src/indexmap/mutable_keys.rs.html#24-29"
class="src rightside">Source</a>

#### fn <a href="#tymethod.get_full_mut2" class="fn">get_full_mut2</a>\<Q\>( &mut self, key: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Q</a>, ) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<(<a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>, &mut Self::<a href="trait.MutableKeys.html#associatedtype.Key"
class="associatedtype"
title="type indexmap::map::MutableKeys::Key">Key</a>, &mut Self::<a href="trait.MutableKeys.html#associatedtype.Value"
class="associatedtype"
title="type indexmap::map::MutableKeys::Value">Value</a>)\>

<div class="where">

where Q:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="../trait.Equivalent.html" class="trait"
title="trait indexmap::Equivalent">Equivalent</a>\<Self::<a href="trait.MutableKeys.html#associatedtype.Key"
class="associatedtype"
title="type indexmap::map::MutableKeys::Key">Key</a>\> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Return item index, mutable reference to key and value

</div>

<div id="tymethod.retain2" class="section method">

<a href="../../src/indexmap/mutable_keys.rs.html#38-40"
class="src rightside">Source</a>

#### fn <a href="#tymethod.retain2" class="fn">retain2</a>\<F\>(&mut self, keep: F)

<div class="where">

where F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(&mut
Self::<a href="trait.MutableKeys.html#associatedtype.Key"
class="associatedtype"
title="type indexmap::map::MutableKeys::Key">Key</a>, &mut
Self::<a href="trait.MutableKeys.html#associatedtype.Value"
class="associatedtype"
title="type indexmap::map::MutableKeys::Value">Value</a>) -\>
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>,

</div>

</div>

<div class="docblock">

Scan through each key-value pair in the map and keep those where the
closure `keep` returns `true`.

The elements are visited in order, and remaining elements keep their
order.

Computes in **O(n)** time (average).

</div>

<div id="tymethod.__private_marker" class="section method">

<a href="../../src/indexmap/mutable_keys.rs.html#45"
class="src rightside">Source</a>

#### fn <a href="#tymethod.__private_marker" class="fn">__private_marker</a>(&self) -\> PrivateMarker

</div>

<div class="docblock">

This method is not useful in itself – it is there to “seal” the trait
for external implementation, so that we can add methods without causing
breaking changes.

</div>

</div>

## Dyn Compatibility<a href="#dyn-compatibility" class="anchor">§</a>

<div class="dyn-compatibility-info">

This trait is **not** [dyn
compatible](https://doc.rust-lang.org/1.92.0/reference/items/traits.html#dyn-compatibility).

*In older versions of Rust, dyn compatibility was called "object
safety", so this trait is not object safe.*

</div>

## Implementors<a href="#implementors" class="anchor">§</a>

<div id="implementors-list">

<div id="impl-MutableKeys-for-IndexMap%3CK,+V,+S%3E"
class="section impl">

<a href="../../src/indexmap/mutable_keys.rs.html#51-75"
class="src rightside">Source</a><a href="#impl-MutableKeys-for-IndexMap%3CK,+V,+S%3E"
class="anchor">§</a>

### impl\<K, V, S\> <a href="trait.MutableKeys.html" class="trait"
title="trait indexmap::map::MutableKeys">MutableKeys</a> for <a href="struct.IndexMap.html" class="struct"
title="struct indexmap::map::IndexMap">IndexMap</a>\<K, V, S\>

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a>, S: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a>,

</div>

<div class="docblock">

Opt-in mutable access to keys.

</div>

</div>

<div class="docblock">

See [`MutableKeys`](trait.MutableKeys.html) for more information.

</div>

<div class="impl-items">

<div id="associatedtype.Key-1"
class="section associatedtype trait-impl">

<a href="../../src/indexmap/mutable_keys.rs.html#56"
class="src rightside">Source</a><a href="#associatedtype.Key-1" class="anchor">§</a>

#### type <a href="#associatedtype.Key" class="associatedtype">Key</a> = K

</div>

<div id="associatedtype.Value-1"
class="section associatedtype trait-impl">

<a href="../../src/indexmap/mutable_keys.rs.html#57"
class="src rightside">Source</a><a href="#associatedtype.Value-1" class="anchor">§</a>

#### type <a href="#associatedtype.Value" class="associatedtype">Value</a> = V

</div>

</div>

</div>

</div>

</div>
