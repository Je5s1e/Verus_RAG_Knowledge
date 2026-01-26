<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[verus_syn](index.html)

</div>

# Struct <span class="struct">Attribute</span> Copy item path

<span class="sub-heading"><a href="../src/verus_syn/attr.rs.html#19-179" class="src">Source</a>
</span>

</div>

``` rust
pub struct Attribute {
    pub pound_token: Pound,
    pub style: AttrStyle,
    pub bracket_token: Bracket,
    pub meta: Meta,
}
```

Expand description

<div class="docblock">

An attribute, like `#[repr(transparent)]`.

  

## <a href="#syntax" class="doc-anchor">§</a>Syntax

Rust has six types of attributes.

- Outer attributes like `#[repr(transparent)]`. These appear outside or
  in front of the item they describe.

- Inner attributes like `#![feature(proc_macro)]`. These appear inside
  of the item they describe, usually a module.

- Outer one-line doc comments like `/// Example`.

- Inner one-line doc comments like `//! Please file an issue`.

- Outer documentation blocks `/** Example */`.

- Inner documentation blocks `/*! Please file an issue */`.

The `style` field of type `AttrStyle` distinguishes whether an attribute
is outer or inner.

Every attribute has a `path` that indicates the intended interpretation
of the rest of the attribute’s contents. The path and the optional
additional contents are represented together in the `meta` field of the
attribute in three possible varieties:

- Meta::Path — attributes whose information content conveys just a path,
  for example the `#[test]` attribute.

- Meta::List — attributes that carry arbitrary tokens after the path,
  surrounded by a delimiter (parenthesis, bracket, or brace). For
  example `#[derive(Copy)]` or `#[precondition(x < 5)]`.

- Meta::NameValue — attributes with an `=` sign after the path, followed
  by a Rust expression. For example `#[path = "sys/windows.rs"]`.

All doc comments are represented in the NameValue style with a path of
“doc”, as this is how they are processed by the compiler and by
`macro_rules!` macros.

<div class="example-wrap">

``` text
#[derive(Copy, Clone)]
  ~~~~~~Path
  ^^^^^^^^^^^^^^^^^^^Meta::List

#[path = "sys/windows.rs"]
  ~~~~Path
  ^^^^^^^^^^^^^^^^^^^^^^^Meta::NameValue

#[test]
  ^^^^Meta::Path
```

</div>

  

## <a href="#parsing-from-tokens-to-attribute" class="doc-anchor">§</a>Parsing from tokens to Attribute

This type does not implement the
[`Parse`](parse/trait.Parse.html "trait verus_syn::parse::Parse") trait
and thus cannot be parsed directly by
[`ParseStream::parse`](parse/struct.ParseBuffer.html#method.parse "method verus_syn::parse::ParseBuffer::parse").
Instead use
[`ParseStream::call`](parse/struct.ParseBuffer.html#method.call "method verus_syn::parse::ParseBuffer::call")
with one of the two parser functions
[`Attribute::parse_outer`](struct.Attribute.html#method.parse_outer "associated function verus_syn::Attribute::parse_outer")
or
[`Attribute::parse_inner`](struct.Attribute.html#method.parse_inner "associated function verus_syn::Attribute::parse_inner")
depending on which you intend to parse.

<div class="example-wrap">

``` rust
use syn::{Attribute, Ident, Result, Token};
use syn::parse::{Parse, ParseStream};

// Parses a unit struct with attributes.
//
//     #[path = "s.tmpl"]
//     struct S;
struct UnitStruct {
    attrs: Vec<Attribute>,
    struct_token: Token![struct],
    name: Ident,
    semi_token: Token![;],
}

impl Parse for UnitStruct {
    fn parse(input: ParseStream) -> Result<Self> {
        Ok(UnitStruct {
            attrs: input.call(Attribute::parse_outer)?,
            struct_token: input.parse()?,
            name: input.parse()?,
            semi_token: input.parse()?,
        })
    }
}
```

</div>

  

## <a href="#parsing-from-attribute-to-structured-arguments"
class="doc-anchor">§</a>Parsing from Attribute to structured arguments

The grammar of attributes in Rust is very flexible, which makes the
syntax tree not that useful on its own. In particular, arguments of the
`Meta::List` variety of attribute are held in an arbitrary
`tokens: TokenStream`. Macros are expected to check the `path` of the
attribute, decide whether they recognize it, and then parse the
remaining tokens according to whatever grammar they wish to require for
that kind of attribute. Use
[`parse_args()`](struct.Attribute.html#method.parse_args "method verus_syn::Attribute::parse_args")
to parse those tokens into the expected data structure.

  

## <a href="#doc-comments" class="doc-anchor">§</a>Doc comments

The compiler transforms doc comments, such as `/// comment` and
`/*! comment */`, into attributes before macros are expanded. Each
comment is expanded into an attribute of the form `#[doc = r"comment"]`.

As an example, the following `mod` items are expanded identically:

<div class="example-wrap">

``` rust
let doc: ItemMod = parse_quote! {
    /// Single line doc comments
    /// We write so many!
    /**
     * Multi-line comments...
     * May span many lines
     */
    mod example {
        //! Of course, they can be inner too
        /*! And fit in a single line */
    }
};
let attr: ItemMod = parse_quote! {
    #[doc = r" Single line doc comments"]
    #[doc = r" We write so many!"]
    #[doc = r"
     * Multi-line comments...
     * May span many lines
     "]
    mod example {
        #![doc = r" Of course, they can be inner too"]
        #![doc = r" And fit in a single line "]
    }
};
assert_eq!(doc, attr);
```

</div>

</div>

## Fields<a href="#fields" class="anchor">§</a>

<span id="structfield.pound_token"
class="structfield section-header"><a href="#structfield.pound_token" class="anchor field">§</a>`pound_token: `<a href="token/struct.Pound.html" class="struct"
title="struct verus_syn::token::Pound"><code>Pound</code></a></span><span id="structfield.style"
class="structfield section-header"><a href="#structfield.style" class="anchor field">§</a>`style: `<a href="enum.AttrStyle.html" class="enum"
title="enum verus_syn::AttrStyle"><code>AttrStyle</code></a></span><span id="structfield.bracket_token"
class="structfield section-header"><a href="#structfield.bracket_token" class="anchor field">§</a>`bracket_token: `<a href="token/struct.Bracket.html" class="struct"
title="struct verus_syn::token::Bracket"><code>Bracket</code></a></span><span id="structfield.meta"
class="structfield section-header"><a href="#structfield.meta" class="anchor field">§</a>`meta: `<a href="enum.Meta.html" class="enum"
title="enum verus_syn::Meta"><code>Meta</code></a></span>

## Implementations<a href="#implementations" class="anchor">§</a>

<div id="implementations-list">

<div id="impl-Attribute" class="section impl">

<a href="../src/verus_syn/attr.rs.html#181-427"
class="src rightside">Source</a><a href="#impl-Attribute" class="anchor">§</a>

### impl <a href="struct.Attribute.html" class="struct"
title="struct verus_syn::Attribute">Attribute</a>

</div>

<div class="impl-items">

<div id="method.path" class="section method">

<a href="../src/verus_syn/attr.rs.html#186-188"
class="src rightside">Source</a>

#### pub fn <a href="#method.path" class="fn">path</a>(&self) -\> &<a href="struct.Path.html" class="struct"
title="struct verus_syn::Path">Path</a>

</div>

<div class="docblock">

Returns the path that identifies the interpretation of this attribute.

For example this would return the `test` in `#[test]`, the `derive` in
`#[derive(Copy)]`, and the `path` in `#[path = "sys/windows.rs"]`.

</div>

<div id="method.parse_args" class="section method">

<a href="../src/verus_syn/attr.rs.html#222-224"
class="src rightside">Source</a>

#### pub fn <a href="#method.parse_args" class="fn">parse_args</a>\<T: <a href="parse/trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a>\>(&self) -\> <a href="type.Result.html" class="type"
title="type verus_syn::Result">Result</a>\<T\>

</div>

<div class="docblock">

Parse the arguments to the attribute as a syntax tree.

This is similar to pulling out the `TokenStream` from `Meta::List` and
doing `syn::parse2::<T>(meta_list.tokens)`, except that using
`parse_args` the error message has a more useful span when `tokens` is
empty.

The surrounding delimiters are *not* included in the input to the
parser.

<div class="example-wrap">

``` text
#[my_attr(value < 5)]
          ^^^^^^^^^ what gets parsed
```

</div>

##### <a href="#example" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
use syn::{parse_quote, Attribute, Expr};

let attr: Attribute = parse_quote! {
    #[precondition(value < 5)]
};

if attr.path().is_ident("precondition") {
    let precondition: Expr = attr.parse_args()?;
    // ...
}
```

</div>

</div>

<div id="method.parse_args_with" class="section method">

<a href="../src/verus_syn/attr.rs.html#245-266"
class="src rightside">Source</a>

#### pub fn <a href="#method.parse_args_with" class="fn">parse_args_with</a>\<F: <a href="parse/trait.Parser.html" class="trait"
title="trait verus_syn::parse::Parser">Parser</a>\>(&self, parser: F) -\> <a href="type.Result.html" class="type"
title="type verus_syn::Result">Result</a>\<F::<a href="parse/trait.Parser.html#associatedtype.Output"
class="associatedtype"
title="type verus_syn::parse::Parser::Output">Output</a>\>

</div>

<div class="docblock">

Parse the arguments to the attribute using the given parser.

##### <a href="#example-1" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
use syn::{parse_quote, Attribute};

let attr: Attribute = parse_quote! {
    #[inception { #[brrrrrrraaaaawwwwrwrrrmrmrmmrmrmmmmm] }]
};

let bwom = attr.parse_args_with(Attribute::parse_outer)?;

// Attribute does not have a Parse impl, so we couldn't directly do:
// let bwom: Attribute = attr.parse_args()?;
```

</div>

</div>

<div id="method.parse_nested_meta" class="section method">

<a href="../src/verus_syn/attr.rs.html#391-396"
class="src rightside">Source</a>

#### pub fn <a href="#method.parse_nested_meta" class="fn">parse_nested_meta</a>( &self, logic: impl <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(<a href="meta/struct.ParseNestedMeta.html" class="struct"
title="struct verus_syn::meta::ParseNestedMeta">ParseNestedMeta</a>\<'\_\>) -\> <a href="type.Result.html" class="type"
title="type verus_syn::Result">Result</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.unit.html"
class="primitive">()</a>\>, ) -\> <a href="type.Result.html" class="type"
title="type verus_syn::Result">Result</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.unit.html"
class="primitive">()</a>\>

</div>

<div class="docblock">

Parse the arguments to the attribute, expecting it to follow the
conventional structure used by most of Rust’s built-in attributes.

The [*Meta Item Attribute
Syntax*](https://doc.rust-lang.org/reference/attributes.html#meta-item-attribute-syntax)
section in the Rust reference explains the convention in more detail.
Not all attributes follow this convention, so
[`parse_args()`](struct.Attribute.html#method.parse_args "method verus_syn::Attribute::parse_args")
is available if you need to parse arbitrarily goofy attribute syntax.

##### <a href="#example-2" class="doc-anchor">§</a>Example

We’ll parse a struct, and then parse some of Rust’s `#[repr]` attribute
syntax.

<div class="example-wrap">

``` rust
use syn::{parenthesized, parse_quote, token, ItemStruct, LitInt};

let input: ItemStruct = parse_quote! {
    #[repr(C, align(4))]
    pub struct MyStruct(u16, u32);
};

let mut repr_c = false;
let mut repr_transparent = false;
let mut repr_align = None::<usize>;
let mut repr_packed = None::<usize>;
for attr in &input.attrs {
    if attr.path().is_ident("repr") {
        attr.parse_nested_meta(|meta| {
            // #[repr(C)]
            if meta.path.is_ident("C") {
                repr_c = true;
                return Ok(());
            }

            // #[repr(transparent)]
            if meta.path.is_ident("transparent") {
                repr_transparent = true;
                return Ok(());
            }

            // #[repr(align(N))]
            if meta.path.is_ident("align") {
                let content;
                parenthesized!(content in meta.input);
                let lit: LitInt = content.parse()?;
                let n: usize = lit.base10_parse()?;
                repr_align = Some(n);
                return Ok(());
            }

            // #[repr(packed)] or #[repr(packed(N))], omitted N means 1
            if meta.path.is_ident("packed") {
                if meta.input.peek(token::Paren) {
                    let content;
                    parenthesized!(content in meta.input);
                    let lit: LitInt = content.parse()?;
                    let n: usize = lit.base10_parse()?;
                    repr_packed = Some(n);
                } else {
                    repr_packed = Some(1);
                }
                return Ok(());
            }

            Err(meta.error("unrecognized repr"))
        })?;
    }
}
```

</div>

##### <a href="#alternatives" class="doc-anchor">§</a>Alternatives

In some cases, for attributes which have nested layers of structured
content, the following less flexible approach might be more convenient:

<div class="example-wrap">

``` rust
use syn::punctuated::Punctuated;
use syn::{parenthesized, token, Error, LitInt, Meta, Token};

let mut repr_c = false;
let mut repr_transparent = false;
let mut repr_align = None::<usize>;
let mut repr_packed = None::<usize>;
for attr in &input.attrs {
    if attr.path().is_ident("repr") {
        let nested = attr.parse_args_with(Punctuated::<Meta, Token![,]>::parse_terminated)?;
        for meta in nested {
            match meta {
                // #[repr(C)]
                Meta::Path(path) if path.is_ident("C") => {
                    repr_c = true;
                }

                // #[repr(align(N))]
                Meta::List(meta) if meta.path.is_ident("align") => {
                    let lit: LitInt = meta.parse_args()?;
                    let n: usize = lit.base10_parse()?;
                    repr_align = Some(n);
                }

                /* ... */

                _ => {
                    return Err(Error::new_spanned(meta, "unrecognized repr"));
                }
            }
        }
    }
}
```

</div>

</div>

<div id="method.parse_outer" class="section method">

<a href="../src/verus_syn/attr.rs.html#406-412"
class="src rightside">Source</a>

#### pub fn <a href="#method.parse_outer" class="fn">parse_outer</a>(input: <a href="parse/type.ParseStream.html" class="type"
title="type verus_syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="type.Result.html" class="type"
title="type verus_syn::Result">Result</a>\<<a href="https://doc.rust-lang.org/1.92.0/alloc/vec/struct.Vec.html"
class="struct" title="struct alloc::vec::Vec">Vec</a>\<Self\>\>

</div>

<div class="docblock">

Parses zero or more outer attributes from the stream.

##### <a href="#example-3" class="doc-anchor">§</a>Example

See [*Parsing from tokens to
Attribute*](#parsing-from-tokens-to-attribute).

</div>

<div id="method.parse_inner" class="section method">

<a href="../src/verus_syn/attr.rs.html#422-426"
class="src rightside">Source</a>

#### pub fn <a href="#method.parse_inner" class="fn">parse_inner</a>(input: <a href="parse/type.ParseStream.html" class="type"
title="type verus_syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="type.Result.html" class="type"
title="type verus_syn::Result">Result</a>\<<a href="https://doc.rust-lang.org/1.92.0/alloc/vec/struct.Vec.html"
class="struct" title="struct alloc::vec::Vec">Vec</a>\<Self\>\>

</div>

<div class="docblock">

Parses zero or more inner attributes from the stream.

##### <a href="#example-4" class="doc-anchor">§</a>Example

See [*Parsing from tokens to
Attribute*](#parsing-from-tokens-to-attribute).

</div>

</div>

</div>

## Trait Implementations<a href="#trait-implementations" class="anchor">§</a>

<div id="trait-implementations-list">

<div id="impl-Clone-for-Attribute" class="section impl">

<a href="../src/verus_syn/gen/clone.rs.html#143-152"
class="src rightside">Source</a><a href="#impl-Clone-for-Attribute" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a> for <a href="struct.Attribute.html" class="struct"
title="struct verus_syn::Attribute">Attribute</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate features `derive` or `full`** only.

</div>

</div>

<div class="impl-items">

<div id="method.clone" class="section method trait-impl">

<a href="../src/verus_syn/gen/clone.rs.html#144-151"
class="src rightside">Source</a><a href="#method.clone" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html#tymethod.clone"
class="fn">clone</a>(&self) -\> Self

</div>

<div class="docblock">

Returns a duplicate of the value. [Read
more](https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html#tymethod.clone)

</div>

<div id="method.clone_from" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/clone.rs.html#245-247"
class="src">Source</a></span><a href="#method.clone_from" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html#method.clone_from"
class="fn">clone_from</a>(&mut self, source: &Self)

</div>

<div class="docblock">

Performs copy-assignment from `source`. [Read
more](https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html#method.clone_from)

</div>

</div>

<div id="impl-Debug-for-Attribute" class="section impl">

<a href="../src/verus_syn/gen/debug.rs.html#155-164"
class="src rightside">Source</a><a href="#impl-Debug-for-Attribute" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a> for <a href="struct.Attribute.html" class="struct"
title="struct verus_syn::Attribute">Attribute</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate features `derive` or `full`** only.

</div>

</div>

<div class="impl-items">

<div id="method.fmt" class="section method trait-impl">

<a href="../src/verus_syn/gen/debug.rs.html#156-163"
class="src rightside">Source</a><a href="#method.fmt" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html#tymethod.fmt"
class="fn">fmt</a>(&self, formatter: &mut <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/struct.Formatter.html"
class="struct" title="struct core::fmt::Formatter">Formatter</a>\<'\_\>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/type.Result.html"
class="type" title="type core::fmt::Result">Result</a>

</div>

<div class="docblock">

Formats the value using the given formatter. [Read
more](https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html#tymethod.fmt)

</div>

</div>

<div id="impl-Hash-for-Attribute" class="section impl">

<a href="../src/verus_syn/gen/hash.rs.html#143-151"
class="src rightside">Source</a><a href="#impl-Hash-for-Attribute" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> for <a href="struct.Attribute.html" class="struct"
title="struct verus_syn::Attribute">Attribute</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate features `derive` or `full`** only.

</div>

</div>

<div class="impl-items">

<div id="method.hash" class="section method trait-impl">

<a href="../src/verus_syn/gen/hash.rs.html#144-150"
class="src rightside">Source</a><a href="#method.hash" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html#tymethod.hash"
class="fn">hash</a>\<H\>(&self, state: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut H</a>)

<div class="where">

where H:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hasher.html"
class="trait" title="trait core::hash::Hasher">Hasher</a>,

</div>

</div>

<div class="docblock">

Feeds this value into the given
[`Hasher`](https://doc.rust-lang.org/1.92.0/core/hash/trait.Hasher.html "trait core::hash::Hasher").
[Read
more](https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html#tymethod.hash)

</div>

<div id="method.hash_slice" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.3.0">1.3.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/hash/mod.rs.html#235-237"
class="src">Source</a></span><a href="#method.hash_slice" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html#method.hash_slice"
class="fn">hash_slice</a>\<H\>(data: &\[Self\], state: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut H</a>)

<div class="where">

where H:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hasher.html"
class="trait" title="trait core::hash::Hasher">Hasher</a>, Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Feeds a slice of this type into the given
[`Hasher`](https://doc.rust-lang.org/1.92.0/core/hash/trait.Hasher.html "trait core::hash::Hasher").
[Read
more](https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html#method.hash_slice)

</div>

</div>

<div id="impl-PartialEq-for-Attribute" class="section impl">

<a href="../src/verus_syn/gen/eq.rs.html#121-125"
class="src rightside">Source</a><a href="#impl-PartialEq-for-Attribute" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialEq.html"
class="trait" title="trait core::cmp::PartialEq">PartialEq</a> for <a href="struct.Attribute.html" class="struct"
title="struct verus_syn::Attribute">Attribute</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate features `derive` or `full`** only.

</div>

</div>

<div class="impl-items">

<div id="method.eq" class="section method trait-impl">

<a href="../src/verus_syn/gen/eq.rs.html#122-124"
class="src rightside">Source</a><a href="#method.eq" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialEq.html#tymethod.eq"
class="fn">eq</a>(&self, other: &Self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Tests for `self` and `other` values to be equal, and is used by `==`.

</div>

<div id="method.ne" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> ·
<a href="https://doc.rust-lang.org/1.92.0/src/core/cmp.rs.html#264"
class="src">Source</a></span><a href="#method.ne" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialEq.html#method.ne"
class="fn">ne</a>(&self, other: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Rhs</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Tests for `!=`. The default implementation is almost always sufficient,
and should not be overridden without very good reason.

</div>

</div>

<div id="impl-ToTokens-for-Attribute" class="section impl">

<a href="../src/verus_syn/attr.rs.html#819-829"
class="src rightside">Source</a><a href="#impl-ToTokens-for-Attribute" class="anchor">§</a>

### impl <a href="../quote/to_tokens/trait.ToTokens.html" class="trait"
title="trait quote::to_tokens::ToTokens">ToTokens</a> for <a href="struct.Attribute.html" class="struct"
title="struct verus_syn::Attribute">Attribute</a>

</div>

<div class="impl-items">

<div id="method.to_tokens" class="section method trait-impl">

<a href="../src/verus_syn/attr.rs.html#820-828"
class="src rightside">Source</a><a href="#method.to_tokens" class="anchor">§</a>

#### fn <a href="../quote/to_tokens/trait.ToTokens.html#tymethod.to_tokens"
class="fn">to_tokens</a>(&self, tokens: &mut <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

<div class="docblock">

Write `self` to the given `TokenStream`. [Read
more](../quote/to_tokens/trait.ToTokens.html#tymethod.to_tokens)

</div>

<div id="method.to_token_stream" class="section method trait-impl">

<a href="../src/quote/to_tokens.rs.html#59"
class="src rightside">Source</a><a href="#method.to_token_stream" class="anchor">§</a>

#### fn <a href="../quote/to_tokens/trait.ToTokens.html#method.to_token_stream"
class="fn">to_token_stream</a>(&self) -\> <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>

</div>

<div class="docblock">

Convert `self` directly into a `TokenStream` object. [Read
more](../quote/to_tokens/trait.ToTokens.html#method.to_token_stream)

</div>

<div id="method.into_token_stream" class="section method trait-impl">

<a href="../src/quote/to_tokens.rs.html#69-71"
class="src rightside">Source</a><a href="#method.into_token_stream" class="anchor">§</a>

#### fn <a
href="../quote/to_tokens/trait.ToTokens.html#method.into_token_stream"
class="fn">into_token_stream</a>(self) -\> <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Convert `self` directly into a `TokenStream` object. [Read
more](../quote/to_tokens/trait.ToTokens.html#method.into_token_stream)

</div>

</div>

<div id="impl-Eq-for-Attribute" class="section impl">

<a href="../src/verus_syn/gen/eq.rs.html#118"
class="src rightside">Source</a><a href="#impl-Eq-for-Attribute" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> for <a href="struct.Attribute.html" class="struct"
title="struct verus_syn::Attribute">Attribute</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate features `derive` or `full`** only.

</div>

</div>

</div>

## Auto Trait Implementations<a href="#synthetic-implementations" class="anchor">§</a>

<div id="synthetic-implementations-list">

<div id="impl-Freeze-for-Attribute" class="section impl">

<a href="#impl-Freeze-for-Attribute" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a> for <a href="struct.Attribute.html" class="struct"
title="struct verus_syn::Attribute">Attribute</a>

</div>

<div id="impl-RefUnwindSafe-for-Attribute" class="section impl">

<a href="#impl-RefUnwindSafe-for-Attribute" class="anchor">§</a>

### impl <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a> for <a href="struct.Attribute.html" class="struct"
title="struct verus_syn::Attribute">Attribute</a>

</div>

<div id="impl-Send-for-Attribute" class="section impl">

<a href="#impl-Send-for-Attribute" class="anchor">§</a>

### impl \!<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a> for <a href="struct.Attribute.html" class="struct"
title="struct verus_syn::Attribute">Attribute</a>

</div>

<div id="impl-Sync-for-Attribute" class="section impl">

<a href="#impl-Sync-for-Attribute" class="anchor">§</a>

### impl \!<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a> for <a href="struct.Attribute.html" class="struct"
title="struct verus_syn::Attribute">Attribute</a>

</div>

<div id="impl-Unpin-for-Attribute" class="section impl">

<a href="#impl-Unpin-for-Attribute" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a> for <a href="struct.Attribute.html" class="struct"
title="struct verus_syn::Attribute">Attribute</a>

</div>

<div id="impl-UnwindSafe-for-Attribute" class="section impl">

<a href="#impl-UnwindSafe-for-Attribute" class="anchor">§</a>

### impl <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a> for <a href="struct.Attribute.html" class="struct"
title="struct verus_syn::Attribute">Attribute</a>

</div>

</div>

## Blanket Implementations<a href="#blanket-implementations" class="anchor">§</a>

<div id="blanket-implementations-list">

<div id="impl-Any-for-T" class="section impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/any.rs.html#138"
class="src rightside">Source</a><a href="#impl-Any-for-T" class="anchor">§</a>

### impl\<T\> <a href="https://doc.rust-lang.org/1.92.0/core/any/trait.Any.html"
class="trait" title="trait core::any::Any">Any</a> for T

<div class="where">

where T: 'static +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="impl-items">

<div id="method.type_id" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/any.rs.html#139"
class="src rightside">Source</a><a href="#method.type_id" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/any/trait.Any.html#tymethod.type_id"
class="fn">type_id</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/any/struct.TypeId.html"
class="struct" title="struct core::any::TypeId">TypeId</a>

</div>

<div class="docblock">

Gets the `TypeId` of `self`. [Read
more](https://doc.rust-lang.org/1.92.0/core/any/trait.Any.html#tymethod.type_id)

</div>

</div>

<div id="impl-Borrow%3CT%3E-for-T" class="section impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/borrow.rs.html#212"
class="src rightside">Source</a><a href="#impl-Borrow%3CT%3E-for-T" class="anchor">§</a>

### impl\<T\> <a href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.Borrow.html"
class="trait" title="trait core::borrow::Borrow">Borrow</a>\<T\> for T

<div class="where">

where T:
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="impl-items">

<div id="method.borrow" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/borrow.rs.html#214"
class="src rightside">Source</a><a href="#method.borrow" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.Borrow.html#tymethod.borrow"
class="fn">borrow</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;T</a>

</div>

<div class="docblock">

Immutably borrows from an owned value. [Read
more](https://doc.rust-lang.org/1.92.0/core/borrow/trait.Borrow.html#tymethod.borrow)

</div>

</div>

<div id="impl-BorrowMut%3CT%3E-for-T" class="section impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/borrow.rs.html#221"
class="src rightside">Source</a><a href="#impl-BorrowMut%3CT%3E-for-T" class="anchor">§</a>

### impl\<T\> <a
href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.BorrowMut.html"
class="trait" title="trait core::borrow::BorrowMut">BorrowMut</a>\<T\> for T

<div class="where">

where T:
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="impl-items">

<div id="method.borrow_mut" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/borrow.rs.html#222"
class="src rightside">Source</a><a href="#method.borrow_mut" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.BorrowMut.html#tymethod.borrow_mut"
class="fn">borrow_mut</a>(&mut self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut T</a>

</div>

<div class="docblock">

Mutably borrows from an owned value. [Read
more](https://doc.rust-lang.org/1.92.0/core/borrow/trait.BorrowMut.html#tymethod.borrow_mut)

</div>

</div>

<div id="impl-CloneToUninit-for-T" class="section impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/clone.rs.html#515"
class="src rightside">Source</a><a href="#impl-CloneToUninit-for-T" class="anchor">§</a>

### impl\<T\> <a
href="https://doc.rust-lang.org/1.92.0/core/clone/trait.CloneToUninit.html"
class="trait" title="trait core::clone::CloneToUninit">CloneToUninit</a> for T

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>,

</div>

</div>

<div class="impl-items">

<div id="method.clone_to_uninit" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/clone.rs.html#517"
class="src rightside">Source</a><a href="#method.clone_to_uninit" class="anchor">§</a>

#### unsafe fn <a
href="https://doc.rust-lang.org/1.92.0/core/clone/trait.CloneToUninit.html#tymethod.clone_to_uninit"
class="fn">clone_to_uninit</a>(&self, dest: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.pointer.html"
class="primitive">*mut</a> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u8.html"
class="primitive">u8</a>)

</div>

<span class="item-info"></span>

<div class="stab unstable">

🔬This is a nightly-only experimental API. (`clone_to_uninit`)

</div>

<div class="docblock">

Performs copy-assignment from `self` to `dest`. [Read
more](https://doc.rust-lang.org/1.92.0/core/clone/trait.CloneToUninit.html#tymethod.clone_to_uninit)

</div>

</div>

<div id="impl-From%3CT%3E-for-T" class="section impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#785"
class="src rightside">Source</a><a href="#impl-From%3CT%3E-for-T" class="anchor">§</a>

### impl\<T\> <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<T\> for T

</div>

<div class="impl-items">

<div id="method.from" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#788"
class="src rightside">Source</a><a href="#method.from" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(t: T) -\> T

</div>

<div class="docblock">

Returns the argument unchanged.

</div>

</div>

<div id="impl-Into%3CU%3E-for-T" class="section impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#767-769"
class="src rightside">Source</a><a href="#impl-Into%3CU%3E-for-T" class="anchor">§</a>

### impl\<T, U\> <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.Into.html"
class="trait" title="trait core::convert::Into">Into</a>\<U\> for T

<div class="where">

where U:
<a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<T\>,

</div>

</div>

<div class="impl-items">

<div id="method.into" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#777"
class="src rightside">Source</a><a href="#method.into" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.Into.html#tymethod.into"
class="fn">into</a>(self) -\> U

</div>

<div class="docblock">

Calls `U::from(self)`.

That is, this conversion is whatever the implementation of
[`From`](https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html "trait core::convert::From")`<T> for U`
chooses to do.

</div>

</div>

<div id="impl-Spanned-for-T" class="section impl">

<a href="../src/verus_syn/spanned.rs.html#104-108"
class="src rightside">Source</a><a href="#impl-Spanned-for-T" class="anchor">§</a>

### impl\<T\> <a href="spanned/trait.Spanned.html" class="trait"
title="trait verus_syn::spanned::Spanned">Spanned</a> for T

<div class="where">

where T: Spanned +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="impl-items">

<div id="method.span" class="section method trait-impl">

<a href="../src/verus_syn/spanned.rs.html#105-107"
class="src rightside">Source</a><a href="#method.span" class="anchor">§</a>

#### fn <a href="spanned/trait.Spanned.html#tymethod.span" class="fn">span</a>(&self) -\> <a href="../proc_macro2/struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>

</div>

<div class="docblock">

Returns a `Span` covering the complete contents of this syntax tree
node, or
[`Span::call_site()`](../proc_macro2/struct.Span.html#method.call_site "associated function proc_macro2::Span::call_site")
if this node is empty.

</div>

</div>

<div id="impl-ToOwned-for-T" class="section impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/alloc/borrow.rs.html#85-87"
class="src rightside">Source</a><a href="#impl-ToOwned-for-T" class="anchor">§</a>

### impl\<T\> <a
href="https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html"
class="trait" title="trait alloc::borrow::ToOwned">ToOwned</a> for T

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>,

</div>

</div>

<div class="impl-items">

<div id="associatedtype.Owned"
class="section associatedtype trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/alloc/borrow.rs.html#89"
class="src rightside">Source</a><a href="#associatedtype.Owned" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html#associatedtype.Owned"
class="associatedtype">Owned</a> = T

</div>

<div class="docblock">

The resulting type after obtaining ownership.

</div>

<div id="method.to_owned" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/alloc/borrow.rs.html#90"
class="src rightside">Source</a><a href="#method.to_owned" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html#tymethod.to_owned"
class="fn">to_owned</a>(&self) -\> T

</div>

<div class="docblock">

Creates owned data from borrowed data, usually by cloning. [Read
more](https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html#tymethod.to_owned)

</div>

<div id="method.clone_into" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/alloc/borrow.rs.html#94"
class="src rightside">Source</a><a href="#method.clone_into" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html#method.clone_into"
class="fn">clone_into</a>(&self, target: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut T</a>)

</div>

<div class="docblock">

Uses borrowed data to replace owned data, usually by cloning. [Read
more](https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html#method.clone_into)

</div>

</div>

<div id="impl-TryFrom%3CU%3E-for-T" class="section impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#827-829"
class="src rightside">Source</a><a href="#impl-TryFrom%3CU%3E-for-T" class="anchor">§</a>

### impl\<T, U\> <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html"
class="trait" title="trait core::convert::TryFrom">TryFrom</a>\<U\> for T

<div class="where">

where U:
<a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.Into.html"
class="trait" title="trait core::convert::Into">Into</a>\<T\>,

</div>

</div>

<div class="impl-items">

<div id="associatedtype.Error-1"
class="section associatedtype trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#831"
class="src rightside">Source</a><a href="#associatedtype.Error-1" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html#associatedtype.Error"
class="associatedtype">Error</a> = <a
href="https://doc.rust-lang.org/1.92.0/core/convert/enum.Infallible.html"
class="enum" title="enum core::convert::Infallible">Infallible</a>

</div>

<div class="docblock">

The type returned in the event of a conversion error.

</div>

<div id="method.try_from" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#834"
class="src rightside">Source</a><a href="#method.try_from" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html#tymethod.try_from"
class="fn">try_from</a>(value: U) -\> <a href="https://doc.rust-lang.org/1.92.0/core/result/enum.Result.html"
class="enum" title="enum core::result::Result">Result</a>\<T, \<T as <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html"
class="trait" title="trait core::convert::TryFrom">TryFrom</a>\<U\>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html#associatedtype.Error"
class="associatedtype"
title="type core::convert::TryFrom::Error">Error</a>\>

</div>

<div class="docblock">

Performs the conversion.

</div>

</div>

<div id="impl-TryInto%3CU%3E-for-T" class="section impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#811-813"
class="src rightside">Source</a><a href="#impl-TryInto%3CU%3E-for-T" class="anchor">§</a>

### impl\<T, U\> <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryInto.html"
class="trait" title="trait core::convert::TryInto">TryInto</a>\<U\> for T

<div class="where">

where U: <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html"
class="trait" title="trait core::convert::TryFrom">TryFrom</a>\<T\>,

</div>

</div>

<div class="impl-items">

<div id="associatedtype.Error"
class="section associatedtype trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#815"
class="src rightside">Source</a><a href="#associatedtype.Error" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryInto.html#associatedtype.Error"
class="associatedtype">Error</a> = \<U as <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html"
class="trait" title="trait core::convert::TryFrom">TryFrom</a>\<T\>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html#associatedtype.Error"
class="associatedtype"
title="type core::convert::TryFrom::Error">Error</a>

</div>

<div class="docblock">

The type returned in the event of a conversion error.

</div>

<div id="method.try_into" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#818"
class="src rightside">Source</a><a href="#method.try_into" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryInto.html#tymethod.try_into"
class="fn">try_into</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/result/enum.Result.html"
class="enum" title="enum core::result::Result">Result</a>\<U, \<U as <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html"
class="trait" title="trait core::convert::TryFrom">TryFrom</a>\<T\>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html#associatedtype.Error"
class="associatedtype"
title="type core::convert::TryFrom::Error">Error</a>\>

</div>

<div class="docblock">

Performs the conversion.

</div>

</div>

</div>

</div>

</div>
