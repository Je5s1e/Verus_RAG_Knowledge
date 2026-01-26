<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[tokens](index.html)

</div>

# Trait <span class="trait">MonotonicCountToken</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/tokens.rs.html#163-175" class="src">Source</a>
</span>

</div>

``` rust
pub trait MonotonicCountToken: Sized { }
```

Expand description

<div class="docblock">

Interface for VerusSync tokens created for a field marked with the
`persistent_count` strategy.

<div>

| VerusSync Strategy | Field type | Token trait                  |
|--------------------|------------|------------------------------|
| `persistent_count` | `nat`      | `MonotonicCountToken + Copy` |

</div>

A token represents a “lower bound” on the field value, which increases
monotonically.

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
