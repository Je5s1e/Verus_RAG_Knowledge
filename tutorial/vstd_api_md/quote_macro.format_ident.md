<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[quote](index.html)

</div>

# Macro <span class="macro">format_ident</span> Copy item path

<span class="sub-heading"><a href="../src/quote/format.rs.html#111-125" class="src">Source</a>
</span>

</div>

``` rust
macro_rules! format_ident {
    ($fmt:expr) => { ... };
    ($fmt:expr, $($rest:tt)*) => { ... };
}
```

Expand description

<div class="docblock">

Formatting macro for constructing `Ident`s.

  

## <a href="#syntax" class="doc-anchor">§</a>Syntax

Syntax is copied from the
[`format!`](https://doc.rust-lang.org/1.92.0/alloc/macro.format.html "macro alloc::format")
macro, supporting both positional and named arguments.

Only a limited set of formatting traits are supported. The current
mapping of format types to traits is:

- `{}` ⇒
  [`IdentFragment`](trait.IdentFragment.html "trait quote::IdentFragment")
- `{:o}` ⇒
  [`Octal`](https://doc.rust-lang.org/1.92.0/core/fmt/trait.Octal.html "trait core::fmt::Octal")
- `{:x}` ⇒
  [`LowerHex`](https://doc.rust-lang.org/1.92.0/core/fmt/trait.LowerHex.html "trait core::fmt::LowerHex")
- `{:X}` ⇒
  [`UpperHex`](https://doc.rust-lang.org/1.92.0/core/fmt/trait.UpperHex.html "trait core::fmt::UpperHex")
- `{:b}` ⇒
  [`Binary`](https://doc.rust-lang.org/1.92.0/core/fmt/trait.Binary.html "trait core::fmt::Binary")

See
[`core::fmt`](https://doc.rust-lang.org/1.92.0/core/fmt/index.html "mod core::fmt")
for more information.

  

## <a href="#identfragment" class="doc-anchor">§</a>IdentFragment

Unlike `format!`, this macro uses the
[`IdentFragment`](trait.IdentFragment.html "trait quote::IdentFragment")
formatting trait by default. This trait is like `Display`, with a few
differences:

- `IdentFragment` is only implemented for a limited set of types, such
  as unsigned integers and strings.
- [`Ident`](../proc_macro2/struct.Ident.html "struct proc_macro2::Ident")
  arguments will have their `r#` prefixes stripped, if present.

  

## <a href="#hygiene" class="doc-anchor">§</a>Hygiene

The [`Span`](../proc_macro2/struct.Span.html "struct proc_macro2::Span")
of the first `Ident` argument is used as the span of the final
identifier, falling back to
[`Span::call_site`](../proc_macro2/struct.Span.html#method.call_site "associated function proc_macro2::Span::call_site")
when no identifiers are provided.

<div class="example-wrap">

``` rust
// If `ident` is an Ident, the span of `my_ident` will be inherited from it.
let my_ident = format_ident!("My{}{}", ident, "IsCool");
assert_eq!(my_ident, "MyIdentIsCool");
```

</div>

Alternatively, the span can be overridden by passing the `span` named
argument.

<div class="example-wrap">

``` rust
let my_span = /* ... */;
format_ident!("MyIdent", span = my_span);
```

</div>

  

## <a href="#panics" class="doc-anchor">§</a>Panics

This method will panic if the resulting formatted string is not a valid
identifier.

  

## <a href="#examples" class="doc-anchor">§</a>Examples

Composing raw and non-raw identifiers:

<div class="example-wrap">

``` rust
let my_ident = format_ident!("My{}", "Ident");
assert_eq!(my_ident, "MyIdent");

let raw = format_ident!("r#Raw");
assert_eq!(raw, "r#Raw");

let my_ident_raw = format_ident!("{}Is{}", my_ident, raw);
assert_eq!(my_ident_raw, "MyIdentIsRaw");
```

</div>

Integer formatting options:

<div class="example-wrap">

``` rust
let num: u32 = 10;

let decimal = format_ident!("Id_{}", num);
assert_eq!(decimal, "Id_10");

let octal = format_ident!("Id_{:o}", num);
assert_eq!(octal, "Id_12");

let binary = format_ident!("Id_{:b}", num);
assert_eq!(binary, "Id_1010");

let lower_hex = format_ident!("Id_{:x}", num);
assert_eq!(lower_hex, "Id_a");

let upper_hex = format_ident!("Id_{:X}", num);
assert_eq!(upper_hex, "Id_A");
```

</div>

</div>

</div>

</div>
