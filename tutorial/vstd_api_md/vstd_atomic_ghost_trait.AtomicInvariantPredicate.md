<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[atomic_ghost](index.html)

</div>

# Trait <span class="trait">AtomicInvariantPredicate</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/atomic_ghost.rs.html#12-14"
class="src">Source</a> </span>

</div>

``` rust
pub trait AtomicInvariantPredicate<K, V, G> { }
```

## Implementors<a href="#implementors" class="anchor">§</a>

<div id="implementors-list">

<div id="impl-AtomicInvariantPredicate%3CTracked%3CInstance%3C(Pred,+CellId),+PointsTo%3CV%3E,+InternalPred%3CV,+Pred%3E%3E%3E,+bool,+flag_exc%3C(Pred,+CellId),+PointsTo%3CV%3E,+InternalPred%3CV,+Pred%3E%3E%3E-for-InvariantPredicate_auto_RwLock_exc"
class="section impl">

<a href="../../src/vstd/rwlock.rs.html#348-351"
class="src rightside">Source</a><a
href="#impl-AtomicInvariantPredicate%3CTracked%3CInstance%3C(Pred,+CellId),+PointsTo%3CV%3E,+InternalPred%3CV,+Pred%3E%3E%3E,+bool,+flag_exc%3C(Pred,+CellId),+PointsTo%3CV%3E,+InternalPred%3CV,+Pred%3E%3E%3E-for-InvariantPredicate_auto_RwLock_exc"
class="anchor">§</a>

### impl\<V, Pred: <a href="../rwlock/trait.RwLockPredicate.html" class="trait"
title="trait vstd::rwlock::RwLockPredicate">RwLockPredicate</a>\<V\>\> <a href="trait.AtomicInvariantPredicate.html" class="trait"
title="trait vstd::atomic_ghost::AtomicInvariantPredicate">AtomicInvariantPredicate</a>\<<a href="../prelude/struct.Tracked.html" class="struct"
title="struct vstd::prelude::Tracked">Tracked</a>\<<a href="../rwlock/RwLockToks/struct.Instance.html" class="struct"
title="struct vstd::rwlock::RwLockToks::Instance">Instance</a>\<(Pred, <a href="../cell/struct.CellId.html" class="struct"
title="struct vstd::cell::CellId">CellId</a>), <a href="../cell/struct.PointsTo.html" class="struct"
title="struct vstd::cell::PointsTo">PointsTo</a>\<V\>, InternalPred\<V, Pred\>\>\>, <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>, <a href="../rwlock/RwLockToks/struct.flag_exc.html" class="struct"
title="struct vstd::rwlock::RwLockToks::flag_exc">flag_exc</a>\<(Pred, <a href="../cell/struct.CellId.html" class="struct"
title="struct vstd::cell::CellId">CellId</a>), <a href="../cell/struct.PointsTo.html" class="struct"
title="struct vstd::cell::PointsTo">PointsTo</a>\<V\>, InternalPred\<V, Pred\>\>\> for <a href="../rwlock/struct.InvariantPredicate_auto_RwLock_exc.html"
class="struct"
title="struct vstd::rwlock::InvariantPredicate_auto_RwLock_exc">InvariantPredicate_auto_RwLock_exc</a>

</div>

<div id="impl-AtomicInvariantPredicate%3CTracked%3CInstance%3C(Pred,+CellId),+PointsTo%3CV%3E,+InternalPred%3CV,+Pred%3E%3E%3E,+usize,+flag_rc%3C(Pred,+CellId),+PointsTo%3CV%3E,+InternalPred%3CV,+Pred%3E%3E%3E-for-InvariantPredicate_auto_RwLock_rc"
class="section impl">

<a href="../../src/vstd/rwlock.rs.html#353-356"
class="src rightside">Source</a><a
href="#impl-AtomicInvariantPredicate%3CTracked%3CInstance%3C(Pred,+CellId),+PointsTo%3CV%3E,+InternalPred%3CV,+Pred%3E%3E%3E,+usize,+flag_rc%3C(Pred,+CellId),+PointsTo%3CV%3E,+InternalPred%3CV,+Pred%3E%3E%3E-for-InvariantPredicate_auto_RwLock_rc"
class="anchor">§</a>

### impl\<V, Pred: <a href="../rwlock/trait.RwLockPredicate.html" class="trait"
title="trait vstd::rwlock::RwLockPredicate">RwLockPredicate</a>\<V\>\> <a href="trait.AtomicInvariantPredicate.html" class="trait"
title="trait vstd::atomic_ghost::AtomicInvariantPredicate">AtomicInvariantPredicate</a>\<<a href="../prelude/struct.Tracked.html" class="struct"
title="struct vstd::prelude::Tracked">Tracked</a>\<<a href="../rwlock/RwLockToks/struct.Instance.html" class="struct"
title="struct vstd::rwlock::RwLockToks::Instance">Instance</a>\<(Pred, <a href="../cell/struct.CellId.html" class="struct"
title="struct vstd::cell::CellId">CellId</a>), <a href="../cell/struct.PointsTo.html" class="struct"
title="struct vstd::cell::PointsTo">PointsTo</a>\<V\>, InternalPred\<V, Pred\>\>\>, <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>, <a href="../rwlock/RwLockToks/struct.flag_rc.html" class="struct"
title="struct vstd::rwlock::RwLockToks::flag_rc">flag_rc</a>\<(Pred, <a href="../cell/struct.CellId.html" class="struct"
title="struct vstd::cell::CellId">CellId</a>), <a href="../cell/struct.PointsTo.html" class="struct"
title="struct vstd::cell::PointsTo">PointsTo</a>\<V\>, InternalPred\<V, Pred\>\>\> for <a href="../rwlock/struct.InvariantPredicate_auto_RwLock_rc.html"
class="struct"
title="struct vstd::rwlock::InvariantPredicate_auto_RwLock_rc">InvariantPredicate_auto_RwLock_rc</a>

</div>

</div>

</div>

</div>
