<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[tokens](index.html)

</div>

# Trait <span class="trait">KeyValueToken</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/tokens.rs.html#85-99" class="src">Source</a>
</span>

</div>

``` rust
pub trait KeyValueToken<Key, Value>: Sized { }
```

Expand description

<div class="docblock">

Interface for VerusSync tokens created for a field marked with the `map`
or `persistent_map` strategies.

<div>

| VerusSync Strategy | Field type | Token trait |
|----|----|----|
| `map` | `Map<K, V>` | [`UniqueKeyValueToken<K, V>`](trait.UniqueKeyValueToken.html "trait vstd::tokens::UniqueKeyValueToken") |
| `persistent_map` | `Map<K, V>` | `KeyValueToken<V> + Copy` |

</div>

For the cases where the tokens are not `Copy`, then token is necessarily
*unique* per-instance, per-key; the sub-trait,
[`UniqueKeyValueToken<V>`](trait.UniqueKeyValueToken.html "trait vstd::tokens::UniqueKeyValueToken"),
provides an additional lemma to prove uniqueness.

Each token represents a *single* key-value pair. To work with a
collection of `KeyValueToken`s, use
[`MapToken`](struct.MapToken.html "struct vstd::tokens::MapToken").

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

</div>

</div>

</div>
