<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[synstructure](index.html)

</div>

# Macro <span class="macro">test_derive</span> Copy item path

<span class="sub-heading"><a href="../src/synstructure/macros.rs.html#210-262"
class="src">Source</a> </span>

</div>

``` rust
macro_rules! test_derive {
    ($name:path { $($i:tt)* } expands to { $($o:tt)* }) => { ... };
    ($name:path { $($i:tt)* } expands to { $($o:tt)* } no_build) => { ... };
}
```

Expand description

<div class="docblock">

Run a test on a custom derive. This macro expands both the original
struct and the expansion to ensure that they compile correctly, and
confirms that feeding the original struct into the named derive will
produce the written output.

You can add `no_build` to the end of the macro invocation to disable
checking that the written code compiles. This is useful in contexts
where the procedural macro cannot depend on the crate where it is used
during tests.

## <a href="#usage" class="doc-anchor">§</a>Usage

<div class="example-wrap">

``` rust
fn test_derive_example(_s: synstructure::Structure)
    -> Result<proc_macro2::TokenStream, syn::Error>
{
    Ok(quote::quote! { const YOUR_OUTPUT: &'static str = "here"; })
}

fn main() {
    synstructure::test_derive!{
        test_derive_example {
            struct A;
        }
        expands to {
            const YOUR_OUTPUT: &'static str = "here";
        }
    }
}
```

</div>

</div>

</div>

</div>
