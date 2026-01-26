<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[verus_syn](../index.html)::[parse](index.html)

</div>

# Trait <span class="trait">Peek</span> Copy item path

<span class="sub-heading"><a href="../../src/verus_syn/lookahead.rs.html#174-178"
class="src">Source</a> </span>

</div>

``` rust
pub trait Peek: Sealed { }
```

Expand description

<div class="docblock">

Types that can be parsed by looking at just one token.

Use
[`ParseStream::peek`](struct.ParseBuffer.html#method.peek "method verus_syn::parse::ParseBuffer::peek")
to peek one of these types in a parse stream without consuming it from
the stream.

This trait is sealed and cannot be implemented for types outside of Syn.

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

<div id="impl-Peek-for-End" class="section impl">

<a href="../../src/verus_syn/lookahead.rs.html#320-322"
class="src rightside">Source</a><a href="#impl-Peek-for-End" class="anchor">§</a>

### impl <a href="trait.Peek.html" class="trait"
title="trait verus_syn::parse::Peek">Peek</a> for <a href="struct.End.html" class="struct"
title="struct verus_syn::parse::End">End</a>

</div>

<div id="impl-Peek-for-F" class="section impl">

<a href="../../src/verus_syn/lookahead.rs.html#334-336"
class="src rightside">Source</a><a href="#impl-Peek-for-F" class="anchor">§</a>

### impl\<F: <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Copy.html"
class="trait" title="trait core::marker::Copy">Copy</a> + <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnOnce.html"
class="trait" title="trait core::ops::function::FnOnce">FnOnce</a>(TokenMarker) -\> T, T: <a href="../token/trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a>\> <a href="trait.Peek.html" class="trait"
title="trait verus_syn::parse::Peek">Peek</a> for F

</div>

</div>

</div>

</div>
