<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[tokens](index.html)

</div>

# Trait <span class="trait">SimpleToken</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/tokens.rs.html#228-234" class="src">Source</a>
</span>

</div>

``` rust
pub trait SimpleToken: Sized { }
```

Expand description

<div class="docblock">

Interface for VerusSync tokens created for a field marked with the
`bool` or `persistent_bool` strategy.

<div>

| VerusSync Strategy | Field type | Token trait |
|----|----|----|
| `bool` | `bool` | [`UniqueSimpleToken<V>`](trait.UniqueSimpleToken.html "trait vstd::tokens::UniqueSimpleToken") |
| `persistent_bool` | `bool` | `SimpleToken<V> + Copy` |

</div>

The token contains no additional data; its presence indicates that the
boolean field is `true`.

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
