<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../../index.html)::[rwlock](../index.html)::[RwLockToks](index.html)

</div>

# Type Alias <span class="type">reader_multiset</span> Copy item path

<span class="sub-heading"><a href="../../../src/vstd/rwlock.rs.html#15-234" class="src">Source</a>
</span>

</div>

``` rust
pub type reader_multiset<K, V, Pred: InvariantPredicate<K, V>> = MultisetToken<V, reader<K, V, Pred>>;
```

## Aliased Type<a href="#aliased-type" class="anchor">§</a>

``` rust
pub struct reader_multiset<K, V, Pred: InvariantPredicate<K, V>> { /* private fields */ }
```

</div>

</div>
