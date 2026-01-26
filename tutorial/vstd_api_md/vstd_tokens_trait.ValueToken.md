<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[tokens](index.html)

</div>

# Trait <span class="trait">ValueToken</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/tokens.rs.html#42-54" class="src">Source</a>
</span>

</div>

``` rust
pub trait ValueToken<Value>: Sized { }
```

Expand description

<div class="docblock">

Interface for VerusSync tokens created for a field marked with the
`variable`, `option` or `persistent_option` strategies.

<div>

| VerusSync Strategy | Field type | Token trait |
|----|----|----|
| `variable` | `V` | [`UniqueValueToken<V>`](trait.UniqueValueToken.html "trait vstd::tokens::UniqueValueToken") |
| `option` | `Option<V>` | [`UniqueValueToken<V>`](trait.UniqueValueToken.html "trait vstd::tokens::UniqueValueToken") |
| `persistent_option` | `Option<V>` | `ValueToken<V> + Copy` |

</div>

For the cases where the tokens are not `Copy`, then token is necessarily
*unique* per-instance; the sub-trait,
[`UniqueValueToken<V>`](trait.UniqueValueToken.html "trait vstd::tokens::UniqueValueToken"),
provides an additional lemma to prove uniqueness.

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

<div id="impl-ValueToken%3Cbool%3E-for-flag_exc%3CK,+V,+Pred%3E"
class="section impl">

<a href="../../src/vstd/rwlock.rs.html#15-234"
class="src rightside">Source</a><a href="#impl-ValueToken%3Cbool%3E-for-flag_exc%3CK,+V,+Pred%3E"
class="anchor">§</a>

### impl\<K, V, Pred: <a href="../invariant/trait.InvariantPredicate.html" class="trait"
title="trait vstd::invariant::InvariantPredicate">InvariantPredicate</a>\<K, V\>\> <a href="trait.ValueToken.html" class="trait"
title="trait vstd::tokens::ValueToken">ValueToken</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>\> for <a href="../rwlock/RwLockToks/struct.flag_exc.html" class="struct"
title="struct vstd::rwlock::RwLockToks::flag_exc">flag_exc</a>\<K, V, Pred\>

</div>

<div id="impl-ValueToken%3C()%3E-for-pending_writer%3CK,+V,+Pred%3E"
class="section impl">

<a href="../../src/vstd/rwlock.rs.html#15-234"
class="src rightside">Source</a><a href="#impl-ValueToken%3C()%3E-for-pending_writer%3CK,+V,+Pred%3E"
class="anchor">§</a>

### impl\<K, V, Pred: <a href="../invariant/trait.InvariantPredicate.html" class="trait"
title="trait vstd::invariant::InvariantPredicate">InvariantPredicate</a>\<K, V\>\> <a href="trait.ValueToken.html" class="trait"
title="trait vstd::tokens::ValueToken">ValueToken</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.unit.html"
class="primitive">()</a>\> for <a href="../rwlock/RwLockToks/struct.pending_writer.html" class="struct"
title="struct vstd::rwlock::RwLockToks::pending_writer">pending_writer</a>\<K, V, Pred\>

</div>

<div id="impl-ValueToken%3C()%3E-for-writer%3CK,+V,+Pred%3E"
class="section impl">

<a href="../../src/vstd/rwlock.rs.html#15-234"
class="src rightside">Source</a><a href="#impl-ValueToken%3C()%3E-for-writer%3CK,+V,+Pred%3E"
class="anchor">§</a>

### impl\<K, V, Pred: <a href="../invariant/trait.InvariantPredicate.html" class="trait"
title="trait vstd::invariant::InvariantPredicate">InvariantPredicate</a>\<K, V\>\> <a href="trait.ValueToken.html" class="trait"
title="trait vstd::tokens::ValueToken">ValueToken</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.unit.html"
class="primitive">()</a>\> for <a href="../rwlock/RwLockToks/struct.writer.html" class="struct"
title="struct vstd::rwlock::RwLockToks::writer">writer</a>\<K, V, Pred\>

</div>

<div id="impl-ValueToken%3Cnat%3E-for-flag_rc%3CK,+V,+Pred%3E"
class="section impl">

<a href="../../src/vstd/rwlock.rs.html#15-234"
class="src rightside">Source</a><a href="#impl-ValueToken%3Cnat%3E-for-flag_rc%3CK,+V,+Pred%3E"
class="anchor">§</a>

### impl\<K, V, Pred: <a href="../invariant/trait.InvariantPredicate.html" class="trait"
title="trait vstd::invariant::InvariantPredicate">InvariantPredicate</a>\<K, V\>\> <a href="trait.ValueToken.html" class="trait"
title="trait vstd::tokens::ValueToken">ValueToken</a>\<<a href="../prelude/struct.nat.html" class="struct"
title="struct vstd::prelude::nat">nat</a>\> for <a href="../rwlock/RwLockToks/struct.flag_rc.html" class="struct"
title="struct vstd::rwlock::RwLockToks::flag_rc">flag_rc</a>\<K, V, Pred\>

</div>

</div>

</div>

</div>
