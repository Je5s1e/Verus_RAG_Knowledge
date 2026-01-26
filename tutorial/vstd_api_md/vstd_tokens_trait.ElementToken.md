<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[tokens](index.html)

</div>

# Trait <span class="trait">ElementToken</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/tokens.rs.html#195-202" class="src">Source</a>
</span>

</div>

``` rust
pub trait ElementToken<Element>: Sized { }
```

Expand description

<div class="docblock">

Interface for VerusSync tokens created for a field marked with the
`set`, `persistent_set` or `multiset` strategies.

<div>

| VerusSync Strategy | Field type | Token trait |
|----|----|----|
| `set` | `Set<V>` | [`UniqueElementToken<V>`](trait.UniqueElementToken.html "trait vstd::tokens::UniqueElementToken") |
| `persistent_set` | `Set<V>` | `ElementToken<V> + Copy` |
| `multiset` | `Multiset<V>` | `ElementToken<V>` |

</div>

Each token represents a single element of the set or multiset.

- For the `set` strategy, the token for any given element is unique.
- For the `persistent_set` strategy, the token for any given element is
  not unique, but is `Copy`.
- For the `multiset` strategy, the tokens are neither unique nor `Copy`,
  as the specific multiplicity of each element must be exact.

To work with a collection of `ElementToken`s, use
[`SetToken`](struct.SetToken.html "struct vstd::tokens::SetToken") or
[`MultisetToken`](struct.MultisetToken.html "struct vstd::tokens::MultisetToken").

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

<div id="impl-ElementToken%3C()%3E-for-pending_reader%3CK,+V,+Pred%3E"
class="section impl">

<a href="../../src/vstd/rwlock.rs.html#15-234"
class="src rightside">Source</a><a href="#impl-ElementToken%3C()%3E-for-pending_reader%3CK,+V,+Pred%3E"
class="anchor">§</a>

### impl\<K, V, Pred: <a href="../invariant/trait.InvariantPredicate.html" class="trait"
title="trait vstd::invariant::InvariantPredicate">InvariantPredicate</a>\<K, V\>\> <a href="trait.ElementToken.html" class="trait"
title="trait vstd::tokens::ElementToken">ElementToken</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.unit.html"
class="primitive">()</a>\> for <a href="../rwlock/RwLockToks/struct.pending_reader.html" class="struct"
title="struct vstd::rwlock::RwLockToks::pending_reader">pending_reader</a>\<K, V, Pred\>

</div>

<div id="impl-ElementToken%3CV%3E-for-reader%3CK,+V,+Pred%3E"
class="section impl">

<a href="../../src/vstd/rwlock.rs.html#15-234"
class="src rightside">Source</a><a href="#impl-ElementToken%3CV%3E-for-reader%3CK,+V,+Pred%3E"
class="anchor">§</a>

### impl\<K, V, Pred: <a href="../invariant/trait.InvariantPredicate.html" class="trait"
title="trait vstd::invariant::InvariantPredicate">InvariantPredicate</a>\<K, V\>\> <a href="trait.ElementToken.html" class="trait"
title="trait vstd::tokens::ElementToken">ElementToken</a>\<V\> for <a href="../rwlock/RwLockToks/struct.reader.html" class="struct"
title="struct vstd::rwlock::RwLockToks::reader">reader</a>\<K, V, Pred\>

</div>

</div>

</div>

</div>
