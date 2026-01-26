<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[rwlock](index.html)

</div>

# Type Alias <span class="type">FieldType_RwLock_exc</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/rwlock.rs.html#262-362" class="src">Source</a>
</span>

</div>

``` rust
pub type FieldType_RwLock_exc<V, Pred> = AtomicBool<FieldType_RwLock_inst<V, Pred>, flag_exc<(Pred, CellId), PointsTo<V>, InternalPred<V, Pred>>, InvariantPredicate_auto_RwLock_exc>;
```

## Aliased Type<a href="#aliased-type" class="anchor">§</a>

``` rust
pub struct FieldType_RwLock_exc<V, Pred> { /* private fields */ }
```

</div>

</div>
