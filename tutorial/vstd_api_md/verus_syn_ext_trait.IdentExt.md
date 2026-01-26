<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[verus_syn](../index.html)::[ext](index.html)

</div>

# Trait <span class="trait">IdentExt</span> Copy item path

<span class="sub-heading"><a href="../../src/verus_syn/ext.rs.html#22-95" class="src">Source</a>
</span>

</div>

``` rust
pub trait IdentExt: Sized + Sealed {
    const peek_any: PeekFn = private::PeekFn;

    // Required methods
    fn parse_any(input: ParseStream<'_>) -> Result<Self>;
    fn unraw(&self) -> Ident;
}
```

Expand description

<div class="docblock">

Additional methods for `Ident` not provided by proc-macro2 or
libproc_macro.

This trait is sealed and cannot be implemented for types outside of Syn.
It is implemented only for `proc_macro2::Ident`.

</div>

## Provided Associated Constants<a href="#provided-associated-consts" class="anchor">§</a>

<div class="methods">

<div id="associatedconstant.peek_any" class="section method">

<a href="../../src/verus_syn/ext.rs.html#65"
class="src rightside">Source</a>

#### const <a href="#associatedconstant.peek_any" class="constant">peek_any</a>: PeekFn = private::PeekFn

</div>

<div class="docblock">

Peeks any identifier including keywords. Usage:
`input.peek(Ident::peek_any)`

This is different from `input.peek(Ident)` which only returns true in
the case of an ident which is not a Rust keyword.

</div>

</div>

## Required Methods<a href="#required-methods" class="anchor">§</a>

<div class="methods">

<div id="tymethod.parse_any" class="section method">

<a href="../../src/verus_syn/ext.rs.html#55"
class="src rightside">Source</a>

#### fn <a href="#tymethod.parse_any" class="fn">parse_any</a>(input: <a href="../parse/type.ParseStream.html" class="type"
title="type verus_syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="../type.Result.html" class="type"
title="type verus_syn::Result">Result</a>\<Self\>

</div>

<div class="docblock">

Parses any identifier including keywords.

This is useful when parsing macro input which allows Rust keywords as
identifiers.

##### <a href="#example" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
use syn::{Error, Ident, Result, Token};
use syn::ext::IdentExt;
use syn::parse::ParseStream;

mod kw {
    syn::custom_keyword!(name);
}

// Parses input that looks like `name = NAME` where `NAME` can be
// any identifier.
//
// Examples:
//
//     name = anything
//     name = impl
fn parse_dsl(input: ParseStream) -> Result<Ident> {
    input.parse::<kw::name>()?;
    input.parse::<Token![=]>()?;
    let name = input.call(Ident::parse_any)?;
    Ok(name)
}
```

</div>

</div>

<div id="tymethod.unraw" class="section method">

<a href="../../src/verus_syn/ext.rs.html#94"
class="src rightside">Source</a>

#### fn <a href="#tymethod.unraw" class="fn">unraw</a>(&self) -\> <a href="../struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>

</div>

<div class="docblock">

Strips the raw marker `r#`, if any, from the beginning of an ident.

- unraw(`x`) = `x`
- unraw(`move`) = `move`
- unraw(`r#move`) = `move`

##### <a href="#example-1" class="doc-anchor">§</a>Example

In the case of interop with other languages like Python that have a
different set of keywords than Rust, we might come across macro input
that involves raw identifiers to refer to ordinary variables in the
other language with a name that happens to be a Rust keyword.

The function below appends an identifier from the caller’s input onto a
fixed prefix. Without using `unraw()`, this would tend to produce
invalid identifiers like `__pyo3_get_r#move`.

<div class="example-wrap">

``` rust
use proc_macro2::Span;
use syn::Ident;
use syn::ext::IdentExt;

fn ident_for_getter(variable: &Ident) -> Ident {
    let getter = format!("__pyo3_get_{}", variable.unraw());
    Ident::new(&getter, Span::call_site())
}
```

</div>

</div>

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

<div id="impl-IdentExt-for-Ident" class="section impl">

<a href="../../src/verus_syn/ext.rs.html#97-114"
class="src rightside">Source</a><a href="#impl-IdentExt-for-Ident" class="anchor">§</a>

### impl <a href="trait.IdentExt.html" class="trait"
title="trait verus_syn::ext::IdentExt">IdentExt</a> for <a href="../struct.Ident.html" class="struct"
title="struct verus_syn::Ident">Ident</a>

</div>

</div>

</div>

</div>
