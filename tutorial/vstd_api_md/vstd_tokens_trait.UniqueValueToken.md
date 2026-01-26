<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[tokens](index.html)

</div>

# Trait <span class="trait">UniqueValueToken</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/tokens.rs.html#59-68" class="src">Source</a>
</span>

</div>

``` rust
pub trait UniqueValueToken<Value>: ValueToken<Value> { }
```

Expand description

<div class="docblock">

Interface for VerusSync tokens created for a field marked with the
`variable` or `option` strategies.

See the super-trait
[`ValueToken`](trait.ValueToken.html "trait vstd::tokens::ValueToken")
for more information.

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

<div id="impl-UniqueValueToken%3Cbool%3E-for-flag_exc%3CK,+V,+Pred%3E"
class="section impl">

<a href="../../src/vstd/rwlock.rs.html#15-234"
class="src rightside">Source</a><a href="#impl-UniqueValueToken%3Cbool%3E-for-flag_exc%3CK,+V,+Pred%3E"
class="anchor">§</a>

### impl\<K, V, Pred: <a href="../invariant/trait.InvariantPredicate.html" class="trait"
title="trait vstd::invariant::InvariantPredicate">InvariantPredicate</a>\<K, V\>\> <a href="trait.UniqueValueToken.html" class="trait"
title="trait vstd::tokens::UniqueValueToken">UniqueValueToken</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>\> for <a href="../rwlock/RwLockToks/struct.flag_exc.html" class="struct"
title="struct vstd::rwlock::RwLockToks::flag_exc">flag_exc</a>\<K, V, Pred\>

</div>

<div id="impl-UniqueValueToken%3C()%3E-for-pending_writer%3CK,+V,+Pred%3E"
class="section impl">

<a href="../../src/vstd/rwlock.rs.html#15-234"
class="src rightside">Source</a><a
href="#impl-UniqueValueToken%3C()%3E-for-pending_writer%3CK,+V,+Pred%3E"
class="anchor">§</a>

### impl\<K, V, Pred: <a href="../invariant/trait.InvariantPredicate.html" class="trait"
title="trait vstd::invariant::InvariantPredicate">InvariantPredicate</a>\<K, V\>\> <a href="trait.UniqueValueToken.html" class="trait"
title="trait vstd::tokens::UniqueValueToken">UniqueValueToken</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.unit.html"
class="primitive">()</a>\> for <a href="../rwlock/RwLockToks/struct.pending_writer.html" class="struct"
title="struct vstd::rwlock::RwLockToks::pending_writer">pending_writer</a>\<K, V, Pred\>

</div>

<div id="impl-UniqueValueToken%3C()%3E-for-writer%3CK,+V,+Pred%3E"
class="section impl">

<a href="../../src/vstd/rwlock.rs.html#15-234"
class="src rightside">Source</a><a href="#impl-UniqueValueToken%3C()%3E-for-writer%3CK,+V,+Pred%3E"
class="anchor">§</a>

### impl\<K, V, Pred: <a href="../invariant/trait.InvariantPredicate.html" class="trait"
title="trait vstd::invariant::InvariantPredicate">InvariantPredicate</a>\<K, V\>\> <a href="trait.UniqueValueToken.html" class="trait"
title="trait vstd::tokens::UniqueValueToken">UniqueValueToken</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.unit.html"
class="primitive">()</a>\> for <a href="../rwlock/RwLockToks/struct.writer.html" class="struct"
title="struct vstd::rwlock::RwLockToks::writer">writer</a>\<K, V, Pred\>

</div>

<div id="impl-UniqueValueToken%3Cnat%3E-for-flag_rc%3CK,+V,+Pred%3E"
class="section impl">

<a href="../../src/vstd/rwlock.rs.html#15-234"
class="src rightside">Source</a><a href="#impl-UniqueValueToken%3Cnat%3E-for-flag_rc%3CK,+V,+Pred%3E"
class="anchor">§</a>

### impl\<K, V, Pred: <a href="../invariant/trait.InvariantPredicate.html" class="trait"
title="trait vstd::invariant::InvariantPredicate">InvariantPredicate</a>\<K, V\>\> <a href="trait.UniqueValueToken.html" class="trait"
title="trait vstd::tokens::UniqueValueToken">UniqueValueToken</a>\<<a href="../prelude/struct.nat.html" class="struct"
title="struct vstd::prelude::nat">nat</a>\> for <a href="../rwlock/RwLockToks/struct.flag_rc.html" class="struct"
title="struct vstd::rwlock::RwLockToks::flag_rc">flag_rc</a>\<K, V, Pred\>

</div>

</div>

</div>

</div>
