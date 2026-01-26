<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[synstructure](index.html)

</div>

# Function <span class="fn">unpretty_print</span> Copy item path

<span class="sub-heading"><a href="../src/synstructure/lib.rs.html#2433-2454"
class="src">Source</a> </span>

</div>

``` rust
pub fn unpretty_print<T: Display>(ts: T) -> String
```

Expand description

<div class="docblock">

Dumps an unpretty version of a tokenstream. Takes any type which
implements `Display`.

This is mostly useful for visualizing the output of a procedural macro,
as it makes it marginally more readable. It is used in the
implementation of `test_derive!` to unprettily print the output.

## <a href="#stability" class="doc-anchor">§</a>Stability

The stability of the output of this function is not guaranteed. Do not
assert that the output of this function does not change between minor
versions.

## <a href="#example" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
assert_eq!(
    synstructure::unpretty_print(quote! {
        const _: () = {
            extern crate krate;
            impl<T, U> krate::Trait for A<T, U>
            where
                Option<U>: krate::Trait,
                U: krate::Trait
            {
                fn a() {}
            }
        };
    }),
    "const _ : (
    )
= {
    extern crate krate ;
    impl < T , U > krate :: Trait for A < T , U > where Option < U > : krate :: Trait , U : krate :: Trait {
        fn a (
            )
        {
            }
        }
    }
;
"
)
```

</div>

</div>

</div>

</div>
