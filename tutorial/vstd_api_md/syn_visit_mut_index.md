<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[syn](../index.html)

</div>

# Module visit_mut Copy item path

<span class="sub-heading"><a href="../../src/syn/gen/visit_mut.rs.html#4-3761"
class="src">Source</a> </span>

</div>

Expand description

<div class="docblock">

Syntax tree traversal to mutate an exclusive borrow of a syntax tree in
place.

Each method of the
[`VisitMut`](trait.VisitMut.html "trait syn::visit_mut::VisitMut") trait
is a hook that can be overridden to customize the behavior when mutating
the corresponding type of node. By default, every method recursively
visits the substructure of the input by invoking the right visitor
method of each of its fields.

<div class="example-wrap">

``` rust
pub trait VisitMut {
    /* ... */

    fn visit_expr_binary_mut(&mut self, node: &mut ExprBinary) {
        visit_expr_binary_mut(self, node);
    }

    /* ... */
}

pub fn visit_expr_binary_mut<V>(v: &mut V, node: &mut ExprBinary)
where
    V: VisitMut + ?Sized,
{
    for attr in &mut node.attrs {
        v.visit_attribute_mut(attr);
    }
    v.visit_expr_mut(&mut *node.left);
    v.visit_bin_op_mut(&mut node.op);
    v.visit_expr_mut(&mut *node.right);
}

/* ... */
```

</div>

  

## <a href="#example" class="doc-anchor">§</a>Example

This mut visitor replace occurrences of u256 suffixed integer literals
like `999u256` with a macro invocation `bigint::u256!(999)`.

<div class="example-wrap">

``` rust
// [dependencies]
// quote = "1.0"
// syn = { version = "2.0", features = ["full", "visit-mut"] }

use quote::quote;
use syn::visit_mut::{self, VisitMut};
use syn::{parse_quote, Expr, File, Lit, LitInt};

struct BigintReplace;

impl VisitMut for BigintReplace {
    fn visit_expr_mut(&mut self, node: &mut Expr) {
        if let Expr::Lit(expr) = &node {
            if let Lit::Int(int) = &expr.lit {
                if int.suffix() == "u256" {
                    let digits = int.base10_digits();
                    let unsuffixed: LitInt = syn::parse_str(digits).unwrap();
                    *node = parse_quote!(bigint::u256!(#unsuffixed));
                    return;
                }
            }
        }

        // Delegate to the default impl to visit nested expressions.
        visit_mut::visit_expr_mut(self, node);
    }
}

fn main() {
    let code = quote! {
        fn main() {
            let _ = 999u256;
        }
    };

    let mut syntax_tree: File = syn::parse2(code).unwrap();
    BigintReplace.visit_file_mut(&mut syntax_tree);
    println!("{}", quote!(#syntax_tree));
}
```

</div>

</div>

## Traits<a href="#traits" class="anchor">§</a>

<a href="trait.VisitMut.html" class="trait"
title="trait syn::visit_mut::VisitMut">VisitMut</a>  
Syntax tree traversal to mutate an exclusive borrow of a syntax tree in
place.

## Functions<a href="#functions" class="anchor">§</a>

<a href="fn.visit_abi_mut.html" class="fn"
title="fn syn::visit_mut::visit_abi_mut">visit_abi_mut</a>

<a href="fn.visit_angle_bracketed_generic_arguments_mut.html" class="fn"
title="fn syn::visit_mut::visit_angle_bracketed_generic_arguments_mut">visit_angle_bracketed_generic_arguments_mut</a>

<a href="fn.visit_arm_mut.html" class="fn"
title="fn syn::visit_mut::visit_arm_mut">visit_arm_mut</a>

<a href="fn.visit_assoc_const_mut.html" class="fn"
title="fn syn::visit_mut::visit_assoc_const_mut">visit_assoc_const_mut</a>

<a href="fn.visit_assoc_type_mut.html" class="fn"
title="fn syn::visit_mut::visit_assoc_type_mut">visit_assoc_type_mut</a>

<a href="fn.visit_attr_style_mut.html" class="fn"
title="fn syn::visit_mut::visit_attr_style_mut">visit_attr_style_mut</a>

<a href="fn.visit_attribute_mut.html" class="fn"
title="fn syn::visit_mut::visit_attribute_mut">visit_attribute_mut</a>

<a href="fn.visit_bare_fn_arg_mut.html" class="fn"
title="fn syn::visit_mut::visit_bare_fn_arg_mut">visit_bare_fn_arg_mut</a>

<a href="fn.visit_bare_variadic_mut.html" class="fn"
title="fn syn::visit_mut::visit_bare_variadic_mut">visit_bare_variadic_mut</a>

<a href="fn.visit_bin_op_mut.html" class="fn"
title="fn syn::visit_mut::visit_bin_op_mut">visit_bin_op_mut</a>

<a href="fn.visit_block_mut.html" class="fn"
title="fn syn::visit_mut::visit_block_mut">visit_block_mut</a>

<a href="fn.visit_bound_lifetimes_mut.html" class="fn"
title="fn syn::visit_mut::visit_bound_lifetimes_mut">visit_bound_lifetimes_mut</a>

<a href="fn.visit_captured_param_mut.html" class="fn"
title="fn syn::visit_mut::visit_captured_param_mut">visit_captured_param_mut</a>

<a href="fn.visit_const_param_mut.html" class="fn"
title="fn syn::visit_mut::visit_const_param_mut">visit_const_param_mut</a>

<a href="fn.visit_constraint_mut.html" class="fn"
title="fn syn::visit_mut::visit_constraint_mut">visit_constraint_mut</a>

<a href="fn.visit_data_enum_mut.html" class="fn"
title="fn syn::visit_mut::visit_data_enum_mut">visit_data_enum_mut</a>

<a href="fn.visit_data_mut.html" class="fn"
title="fn syn::visit_mut::visit_data_mut">visit_data_mut</a>

<a href="fn.visit_data_struct_mut.html" class="fn"
title="fn syn::visit_mut::visit_data_struct_mut">visit_data_struct_mut</a>

<a href="fn.visit_data_union_mut.html" class="fn"
title="fn syn::visit_mut::visit_data_union_mut">visit_data_union_mut</a>

<a href="fn.visit_derive_input_mut.html" class="fn"
title="fn syn::visit_mut::visit_derive_input_mut">visit_derive_input_mut</a>

<a href="fn.visit_expr_array_mut.html" class="fn"
title="fn syn::visit_mut::visit_expr_array_mut">visit_expr_array_mut</a>

<a href="fn.visit_expr_assign_mut.html" class="fn"
title="fn syn::visit_mut::visit_expr_assign_mut">visit_expr_assign_mut</a>

<a href="fn.visit_expr_async_mut.html" class="fn"
title="fn syn::visit_mut::visit_expr_async_mut">visit_expr_async_mut</a>

<a href="fn.visit_expr_await_mut.html" class="fn"
title="fn syn::visit_mut::visit_expr_await_mut">visit_expr_await_mut</a>

<a href="fn.visit_expr_binary_mut.html" class="fn"
title="fn syn::visit_mut::visit_expr_binary_mut">visit_expr_binary_mut</a>

<a href="fn.visit_expr_block_mut.html" class="fn"
title="fn syn::visit_mut::visit_expr_block_mut">visit_expr_block_mut</a>

<a href="fn.visit_expr_break_mut.html" class="fn"
title="fn syn::visit_mut::visit_expr_break_mut">visit_expr_break_mut</a>

<a href="fn.visit_expr_call_mut.html" class="fn"
title="fn syn::visit_mut::visit_expr_call_mut">visit_expr_call_mut</a>

<a href="fn.visit_expr_cast_mut.html" class="fn"
title="fn syn::visit_mut::visit_expr_cast_mut">visit_expr_cast_mut</a>

<a href="fn.visit_expr_closure_mut.html" class="fn"
title="fn syn::visit_mut::visit_expr_closure_mut">visit_expr_closure_mut</a>

<a href="fn.visit_expr_const_mut.html" class="fn"
title="fn syn::visit_mut::visit_expr_const_mut">visit_expr_const_mut</a>

<a href="fn.visit_expr_continue_mut.html" class="fn"
title="fn syn::visit_mut::visit_expr_continue_mut">visit_expr_continue_mut</a>

<a href="fn.visit_expr_field_mut.html" class="fn"
title="fn syn::visit_mut::visit_expr_field_mut">visit_expr_field_mut</a>

<a href="fn.visit_expr_for_loop_mut.html" class="fn"
title="fn syn::visit_mut::visit_expr_for_loop_mut">visit_expr_for_loop_mut</a>

<a href="fn.visit_expr_group_mut.html" class="fn"
title="fn syn::visit_mut::visit_expr_group_mut">visit_expr_group_mut</a>

<a href="fn.visit_expr_if_mut.html" class="fn"
title="fn syn::visit_mut::visit_expr_if_mut">visit_expr_if_mut</a>

<a href="fn.visit_expr_index_mut.html" class="fn"
title="fn syn::visit_mut::visit_expr_index_mut">visit_expr_index_mut</a>

<a href="fn.visit_expr_infer_mut.html" class="fn"
title="fn syn::visit_mut::visit_expr_infer_mut">visit_expr_infer_mut</a>

<a href="fn.visit_expr_let_mut.html" class="fn"
title="fn syn::visit_mut::visit_expr_let_mut">visit_expr_let_mut</a>

<a href="fn.visit_expr_lit_mut.html" class="fn"
title="fn syn::visit_mut::visit_expr_lit_mut">visit_expr_lit_mut</a>

<a href="fn.visit_expr_loop_mut.html" class="fn"
title="fn syn::visit_mut::visit_expr_loop_mut">visit_expr_loop_mut</a>

<a href="fn.visit_expr_macro_mut.html" class="fn"
title="fn syn::visit_mut::visit_expr_macro_mut">visit_expr_macro_mut</a>

<a href="fn.visit_expr_match_mut.html" class="fn"
title="fn syn::visit_mut::visit_expr_match_mut">visit_expr_match_mut</a>

<a href="fn.visit_expr_method_call_mut.html" class="fn"
title="fn syn::visit_mut::visit_expr_method_call_mut">visit_expr_method_call_mut</a>

<a href="fn.visit_expr_mut.html" class="fn"
title="fn syn::visit_mut::visit_expr_mut">visit_expr_mut</a>

<a href="fn.visit_expr_paren_mut.html" class="fn"
title="fn syn::visit_mut::visit_expr_paren_mut">visit_expr_paren_mut</a>

<a href="fn.visit_expr_path_mut.html" class="fn"
title="fn syn::visit_mut::visit_expr_path_mut">visit_expr_path_mut</a>

<a href="fn.visit_expr_range_mut.html" class="fn"
title="fn syn::visit_mut::visit_expr_range_mut">visit_expr_range_mut</a>

<a href="fn.visit_expr_raw_addr_mut.html" class="fn"
title="fn syn::visit_mut::visit_expr_raw_addr_mut">visit_expr_raw_addr_mut</a>

<a href="fn.visit_expr_reference_mut.html" class="fn"
title="fn syn::visit_mut::visit_expr_reference_mut">visit_expr_reference_mut</a>

<a href="fn.visit_expr_repeat_mut.html" class="fn"
title="fn syn::visit_mut::visit_expr_repeat_mut">visit_expr_repeat_mut</a>

<a href="fn.visit_expr_return_mut.html" class="fn"
title="fn syn::visit_mut::visit_expr_return_mut">visit_expr_return_mut</a>

<a href="fn.visit_expr_struct_mut.html" class="fn"
title="fn syn::visit_mut::visit_expr_struct_mut">visit_expr_struct_mut</a>

<a href="fn.visit_expr_try_block_mut.html" class="fn"
title="fn syn::visit_mut::visit_expr_try_block_mut">visit_expr_try_block_mut</a>

<a href="fn.visit_expr_try_mut.html" class="fn"
title="fn syn::visit_mut::visit_expr_try_mut">visit_expr_try_mut</a>

<a href="fn.visit_expr_tuple_mut.html" class="fn"
title="fn syn::visit_mut::visit_expr_tuple_mut">visit_expr_tuple_mut</a>

<a href="fn.visit_expr_unary_mut.html" class="fn"
title="fn syn::visit_mut::visit_expr_unary_mut">visit_expr_unary_mut</a>

<a href="fn.visit_expr_unsafe_mut.html" class="fn"
title="fn syn::visit_mut::visit_expr_unsafe_mut">visit_expr_unsafe_mut</a>

<a href="fn.visit_expr_while_mut.html" class="fn"
title="fn syn::visit_mut::visit_expr_while_mut">visit_expr_while_mut</a>

<a href="fn.visit_expr_yield_mut.html" class="fn"
title="fn syn::visit_mut::visit_expr_yield_mut">visit_expr_yield_mut</a>

<a href="fn.visit_field_mut.html" class="fn"
title="fn syn::visit_mut::visit_field_mut">visit_field_mut</a>

<a href="fn.visit_field_mutability_mut.html" class="fn"
title="fn syn::visit_mut::visit_field_mutability_mut">visit_field_mutability_mut</a>

<a href="fn.visit_field_pat_mut.html" class="fn"
title="fn syn::visit_mut::visit_field_pat_mut">visit_field_pat_mut</a>

<a href="fn.visit_field_value_mut.html" class="fn"
title="fn syn::visit_mut::visit_field_value_mut">visit_field_value_mut</a>

<a href="fn.visit_fields_mut.html" class="fn"
title="fn syn::visit_mut::visit_fields_mut">visit_fields_mut</a>

<a href="fn.visit_fields_named_mut.html" class="fn"
title="fn syn::visit_mut::visit_fields_named_mut">visit_fields_named_mut</a>

<a href="fn.visit_fields_unnamed_mut.html" class="fn"
title="fn syn::visit_mut::visit_fields_unnamed_mut">visit_fields_unnamed_mut</a>

<a href="fn.visit_file_mut.html" class="fn"
title="fn syn::visit_mut::visit_file_mut">visit_file_mut</a>

<a href="fn.visit_fn_arg_mut.html" class="fn"
title="fn syn::visit_mut::visit_fn_arg_mut">visit_fn_arg_mut</a>

<a href="fn.visit_foreign_item_fn_mut.html" class="fn"
title="fn syn::visit_mut::visit_foreign_item_fn_mut">visit_foreign_item_fn_mut</a>

<a href="fn.visit_foreign_item_macro_mut.html" class="fn"
title="fn syn::visit_mut::visit_foreign_item_macro_mut">visit_foreign_item_macro_mut</a>

<a href="fn.visit_foreign_item_mut.html" class="fn"
title="fn syn::visit_mut::visit_foreign_item_mut">visit_foreign_item_mut</a>

<a href="fn.visit_foreign_item_static_mut.html" class="fn"
title="fn syn::visit_mut::visit_foreign_item_static_mut">visit_foreign_item_static_mut</a>

<a href="fn.visit_foreign_item_type_mut.html" class="fn"
title="fn syn::visit_mut::visit_foreign_item_type_mut">visit_foreign_item_type_mut</a>

<a href="fn.visit_generic_argument_mut.html" class="fn"
title="fn syn::visit_mut::visit_generic_argument_mut">visit_generic_argument_mut</a>

<a href="fn.visit_generic_param_mut.html" class="fn"
title="fn syn::visit_mut::visit_generic_param_mut">visit_generic_param_mut</a>

<a href="fn.visit_generics_mut.html" class="fn"
title="fn syn::visit_mut::visit_generics_mut">visit_generics_mut</a>

<a href="fn.visit_ident_mut.html" class="fn"
title="fn syn::visit_mut::visit_ident_mut">visit_ident_mut</a>

<a href="fn.visit_impl_item_const_mut.html" class="fn"
title="fn syn::visit_mut::visit_impl_item_const_mut">visit_impl_item_const_mut</a>

<a href="fn.visit_impl_item_fn_mut.html" class="fn"
title="fn syn::visit_mut::visit_impl_item_fn_mut">visit_impl_item_fn_mut</a>

<a href="fn.visit_impl_item_macro_mut.html" class="fn"
title="fn syn::visit_mut::visit_impl_item_macro_mut">visit_impl_item_macro_mut</a>

<a href="fn.visit_impl_item_mut.html" class="fn"
title="fn syn::visit_mut::visit_impl_item_mut">visit_impl_item_mut</a>

<a href="fn.visit_impl_item_type_mut.html" class="fn"
title="fn syn::visit_mut::visit_impl_item_type_mut">visit_impl_item_type_mut</a>

<a href="fn.visit_impl_restriction_mut.html" class="fn"
title="fn syn::visit_mut::visit_impl_restriction_mut">visit_impl_restriction_mut</a>

<a href="fn.visit_index_mut.html" class="fn"
title="fn syn::visit_mut::visit_index_mut">visit_index_mut</a>

<a href="fn.visit_item_const_mut.html" class="fn"
title="fn syn::visit_mut::visit_item_const_mut">visit_item_const_mut</a>

<a href="fn.visit_item_enum_mut.html" class="fn"
title="fn syn::visit_mut::visit_item_enum_mut">visit_item_enum_mut</a>

<a href="fn.visit_item_extern_crate_mut.html" class="fn"
title="fn syn::visit_mut::visit_item_extern_crate_mut">visit_item_extern_crate_mut</a>

<a href="fn.visit_item_fn_mut.html" class="fn"
title="fn syn::visit_mut::visit_item_fn_mut">visit_item_fn_mut</a>

<a href="fn.visit_item_foreign_mod_mut.html" class="fn"
title="fn syn::visit_mut::visit_item_foreign_mod_mut">visit_item_foreign_mod_mut</a>

<a href="fn.visit_item_impl_mut.html" class="fn"
title="fn syn::visit_mut::visit_item_impl_mut">visit_item_impl_mut</a>

<a href="fn.visit_item_macro_mut.html" class="fn"
title="fn syn::visit_mut::visit_item_macro_mut">visit_item_macro_mut</a>

<a href="fn.visit_item_mod_mut.html" class="fn"
title="fn syn::visit_mut::visit_item_mod_mut">visit_item_mod_mut</a>

<a href="fn.visit_item_mut.html" class="fn"
title="fn syn::visit_mut::visit_item_mut">visit_item_mut</a>

<a href="fn.visit_item_static_mut.html" class="fn"
title="fn syn::visit_mut::visit_item_static_mut">visit_item_static_mut</a>

<a href="fn.visit_item_struct_mut.html" class="fn"
title="fn syn::visit_mut::visit_item_struct_mut">visit_item_struct_mut</a>

<a href="fn.visit_item_trait_alias_mut.html" class="fn"
title="fn syn::visit_mut::visit_item_trait_alias_mut">visit_item_trait_alias_mut</a>

<a href="fn.visit_item_trait_mut.html" class="fn"
title="fn syn::visit_mut::visit_item_trait_mut">visit_item_trait_mut</a>

<a href="fn.visit_item_type_mut.html" class="fn"
title="fn syn::visit_mut::visit_item_type_mut">visit_item_type_mut</a>

<a href="fn.visit_item_union_mut.html" class="fn"
title="fn syn::visit_mut::visit_item_union_mut">visit_item_union_mut</a>

<a href="fn.visit_item_use_mut.html" class="fn"
title="fn syn::visit_mut::visit_item_use_mut">visit_item_use_mut</a>

<a href="fn.visit_label_mut.html" class="fn"
title="fn syn::visit_mut::visit_label_mut">visit_label_mut</a>

<a href="fn.visit_lifetime_mut.html" class="fn"
title="fn syn::visit_mut::visit_lifetime_mut">visit_lifetime_mut</a>

<a href="fn.visit_lifetime_param_mut.html" class="fn"
title="fn syn::visit_mut::visit_lifetime_param_mut">visit_lifetime_param_mut</a>

<a href="fn.visit_lit_bool_mut.html" class="fn"
title="fn syn::visit_mut::visit_lit_bool_mut">visit_lit_bool_mut</a>

<a href="fn.visit_lit_byte_mut.html" class="fn"
title="fn syn::visit_mut::visit_lit_byte_mut">visit_lit_byte_mut</a>

<a href="fn.visit_lit_byte_str_mut.html" class="fn"
title="fn syn::visit_mut::visit_lit_byte_str_mut">visit_lit_byte_str_mut</a>

<a href="fn.visit_lit_char_mut.html" class="fn"
title="fn syn::visit_mut::visit_lit_char_mut">visit_lit_char_mut</a>

<a href="fn.visit_lit_cstr_mut.html" class="fn"
title="fn syn::visit_mut::visit_lit_cstr_mut">visit_lit_cstr_mut</a>

<a href="fn.visit_lit_float_mut.html" class="fn"
title="fn syn::visit_mut::visit_lit_float_mut">visit_lit_float_mut</a>

<a href="fn.visit_lit_int_mut.html" class="fn"
title="fn syn::visit_mut::visit_lit_int_mut">visit_lit_int_mut</a>

<a href="fn.visit_lit_mut.html" class="fn"
title="fn syn::visit_mut::visit_lit_mut">visit_lit_mut</a>

<a href="fn.visit_lit_str_mut.html" class="fn"
title="fn syn::visit_mut::visit_lit_str_mut">visit_lit_str_mut</a>

<a href="fn.visit_local_init_mut.html" class="fn"
title="fn syn::visit_mut::visit_local_init_mut">visit_local_init_mut</a>

<a href="fn.visit_local_mut.html" class="fn"
title="fn syn::visit_mut::visit_local_mut">visit_local_mut</a>

<a href="fn.visit_macro_delimiter_mut.html" class="fn"
title="fn syn::visit_mut::visit_macro_delimiter_mut">visit_macro_delimiter_mut</a>

<a href="fn.visit_macro_mut.html" class="fn"
title="fn syn::visit_mut::visit_macro_mut">visit_macro_mut</a>

<a href="fn.visit_member_mut.html" class="fn"
title="fn syn::visit_mut::visit_member_mut">visit_member_mut</a>

<a href="fn.visit_meta_list_mut.html" class="fn"
title="fn syn::visit_mut::visit_meta_list_mut">visit_meta_list_mut</a>

<a href="fn.visit_meta_mut.html" class="fn"
title="fn syn::visit_mut::visit_meta_mut">visit_meta_mut</a>

<a href="fn.visit_meta_name_value_mut.html" class="fn"
title="fn syn::visit_mut::visit_meta_name_value_mut">visit_meta_name_value_mut</a>

<a href="fn.visit_parenthesized_generic_arguments_mut.html" class="fn"
title="fn syn::visit_mut::visit_parenthesized_generic_arguments_mut">visit_parenthesized_generic_arguments_mut</a>

<a href="fn.visit_pat_ident_mut.html" class="fn"
title="fn syn::visit_mut::visit_pat_ident_mut">visit_pat_ident_mut</a>

<a href="fn.visit_pat_mut.html" class="fn"
title="fn syn::visit_mut::visit_pat_mut">visit_pat_mut</a>

<a href="fn.visit_pat_or_mut.html" class="fn"
title="fn syn::visit_mut::visit_pat_or_mut">visit_pat_or_mut</a>

<a href="fn.visit_pat_paren_mut.html" class="fn"
title="fn syn::visit_mut::visit_pat_paren_mut">visit_pat_paren_mut</a>

<a href="fn.visit_pat_reference_mut.html" class="fn"
title="fn syn::visit_mut::visit_pat_reference_mut">visit_pat_reference_mut</a>

<a href="fn.visit_pat_rest_mut.html" class="fn"
title="fn syn::visit_mut::visit_pat_rest_mut">visit_pat_rest_mut</a>

<a href="fn.visit_pat_slice_mut.html" class="fn"
title="fn syn::visit_mut::visit_pat_slice_mut">visit_pat_slice_mut</a>

<a href="fn.visit_pat_struct_mut.html" class="fn"
title="fn syn::visit_mut::visit_pat_struct_mut">visit_pat_struct_mut</a>

<a href="fn.visit_pat_tuple_mut.html" class="fn"
title="fn syn::visit_mut::visit_pat_tuple_mut">visit_pat_tuple_mut</a>

<a href="fn.visit_pat_tuple_struct_mut.html" class="fn"
title="fn syn::visit_mut::visit_pat_tuple_struct_mut">visit_pat_tuple_struct_mut</a>

<a href="fn.visit_pat_type_mut.html" class="fn"
title="fn syn::visit_mut::visit_pat_type_mut">visit_pat_type_mut</a>

<a href="fn.visit_pat_wild_mut.html" class="fn"
title="fn syn::visit_mut::visit_pat_wild_mut">visit_pat_wild_mut</a>

<a href="fn.visit_path_arguments_mut.html" class="fn"
title="fn syn::visit_mut::visit_path_arguments_mut">visit_path_arguments_mut</a>

<a href="fn.visit_path_mut.html" class="fn"
title="fn syn::visit_mut::visit_path_mut">visit_path_mut</a>

<a href="fn.visit_path_segment_mut.html" class="fn"
title="fn syn::visit_mut::visit_path_segment_mut">visit_path_segment_mut</a>

<a href="fn.visit_pointer_mutability_mut.html" class="fn"
title="fn syn::visit_mut::visit_pointer_mutability_mut">visit_pointer_mutability_mut</a>

<a href="fn.visit_precise_capture_mut.html" class="fn"
title="fn syn::visit_mut::visit_precise_capture_mut">visit_precise_capture_mut</a>

<a href="fn.visit_predicate_lifetime_mut.html" class="fn"
title="fn syn::visit_mut::visit_predicate_lifetime_mut">visit_predicate_lifetime_mut</a>

<a href="fn.visit_predicate_type_mut.html" class="fn"
title="fn syn::visit_mut::visit_predicate_type_mut">visit_predicate_type_mut</a>

<a href="fn.visit_qself_mut.html" class="fn"
title="fn syn::visit_mut::visit_qself_mut">visit_qself_mut</a>

<a href="fn.visit_range_limits_mut.html" class="fn"
title="fn syn::visit_mut::visit_range_limits_mut">visit_range_limits_mut</a>

<a href="fn.visit_receiver_mut.html" class="fn"
title="fn syn::visit_mut::visit_receiver_mut">visit_receiver_mut</a>

<a href="fn.visit_return_type_mut.html" class="fn"
title="fn syn::visit_mut::visit_return_type_mut">visit_return_type_mut</a>

<a href="fn.visit_signature_mut.html" class="fn"
title="fn syn::visit_mut::visit_signature_mut">visit_signature_mut</a>

<a href="fn.visit_span_mut.html" class="fn"
title="fn syn::visit_mut::visit_span_mut">visit_span_mut</a>

<a href="fn.visit_static_mutability_mut.html" class="fn"
title="fn syn::visit_mut::visit_static_mutability_mut">visit_static_mutability_mut</a>

<a href="fn.visit_stmt_macro_mut.html" class="fn"
title="fn syn::visit_mut::visit_stmt_macro_mut">visit_stmt_macro_mut</a>

<a href="fn.visit_stmt_mut.html" class="fn"
title="fn syn::visit_mut::visit_stmt_mut">visit_stmt_mut</a>

<a href="fn.visit_trait_bound_modifier_mut.html" class="fn"
title="fn syn::visit_mut::visit_trait_bound_modifier_mut">visit_trait_bound_modifier_mut</a>

<a href="fn.visit_trait_bound_mut.html" class="fn"
title="fn syn::visit_mut::visit_trait_bound_mut">visit_trait_bound_mut</a>

<a href="fn.visit_trait_item_const_mut.html" class="fn"
title="fn syn::visit_mut::visit_trait_item_const_mut">visit_trait_item_const_mut</a>

<a href="fn.visit_trait_item_fn_mut.html" class="fn"
title="fn syn::visit_mut::visit_trait_item_fn_mut">visit_trait_item_fn_mut</a>

<a href="fn.visit_trait_item_macro_mut.html" class="fn"
title="fn syn::visit_mut::visit_trait_item_macro_mut">visit_trait_item_macro_mut</a>

<a href="fn.visit_trait_item_mut.html" class="fn"
title="fn syn::visit_mut::visit_trait_item_mut">visit_trait_item_mut</a>

<a href="fn.visit_trait_item_type_mut.html" class="fn"
title="fn syn::visit_mut::visit_trait_item_type_mut">visit_trait_item_type_mut</a>

<a href="fn.visit_type_array_mut.html" class="fn"
title="fn syn::visit_mut::visit_type_array_mut">visit_type_array_mut</a>

<a href="fn.visit_type_bare_fn_mut.html" class="fn"
title="fn syn::visit_mut::visit_type_bare_fn_mut">visit_type_bare_fn_mut</a>

<a href="fn.visit_type_group_mut.html" class="fn"
title="fn syn::visit_mut::visit_type_group_mut">visit_type_group_mut</a>

<a href="fn.visit_type_impl_trait_mut.html" class="fn"
title="fn syn::visit_mut::visit_type_impl_trait_mut">visit_type_impl_trait_mut</a>

<a href="fn.visit_type_infer_mut.html" class="fn"
title="fn syn::visit_mut::visit_type_infer_mut">visit_type_infer_mut</a>

<a href="fn.visit_type_macro_mut.html" class="fn"
title="fn syn::visit_mut::visit_type_macro_mut">visit_type_macro_mut</a>

<a href="fn.visit_type_mut.html" class="fn"
title="fn syn::visit_mut::visit_type_mut">visit_type_mut</a>

<a href="fn.visit_type_never_mut.html" class="fn"
title="fn syn::visit_mut::visit_type_never_mut">visit_type_never_mut</a>

<a href="fn.visit_type_param_bound_mut.html" class="fn"
title="fn syn::visit_mut::visit_type_param_bound_mut">visit_type_param_bound_mut</a>

<a href="fn.visit_type_param_mut.html" class="fn"
title="fn syn::visit_mut::visit_type_param_mut">visit_type_param_mut</a>

<a href="fn.visit_type_paren_mut.html" class="fn"
title="fn syn::visit_mut::visit_type_paren_mut">visit_type_paren_mut</a>

<a href="fn.visit_type_path_mut.html" class="fn"
title="fn syn::visit_mut::visit_type_path_mut">visit_type_path_mut</a>

<a href="fn.visit_type_ptr_mut.html" class="fn"
title="fn syn::visit_mut::visit_type_ptr_mut">visit_type_ptr_mut</a>

<a href="fn.visit_type_reference_mut.html" class="fn"
title="fn syn::visit_mut::visit_type_reference_mut">visit_type_reference_mut</a>

<a href="fn.visit_type_slice_mut.html" class="fn"
title="fn syn::visit_mut::visit_type_slice_mut">visit_type_slice_mut</a>

<a href="fn.visit_type_trait_object_mut.html" class="fn"
title="fn syn::visit_mut::visit_type_trait_object_mut">visit_type_trait_object_mut</a>

<a href="fn.visit_type_tuple_mut.html" class="fn"
title="fn syn::visit_mut::visit_type_tuple_mut">visit_type_tuple_mut</a>

<a href="fn.visit_un_op_mut.html" class="fn"
title="fn syn::visit_mut::visit_un_op_mut">visit_un_op_mut</a>

<a href="fn.visit_use_glob_mut.html" class="fn"
title="fn syn::visit_mut::visit_use_glob_mut">visit_use_glob_mut</a>

<a href="fn.visit_use_group_mut.html" class="fn"
title="fn syn::visit_mut::visit_use_group_mut">visit_use_group_mut</a>

<a href="fn.visit_use_name_mut.html" class="fn"
title="fn syn::visit_mut::visit_use_name_mut">visit_use_name_mut</a>

<a href="fn.visit_use_path_mut.html" class="fn"
title="fn syn::visit_mut::visit_use_path_mut">visit_use_path_mut</a>

<a href="fn.visit_use_rename_mut.html" class="fn"
title="fn syn::visit_mut::visit_use_rename_mut">visit_use_rename_mut</a>

<a href="fn.visit_use_tree_mut.html" class="fn"
title="fn syn::visit_mut::visit_use_tree_mut">visit_use_tree_mut</a>

<a href="fn.visit_variadic_mut.html" class="fn"
title="fn syn::visit_mut::visit_variadic_mut">visit_variadic_mut</a>

<a href="fn.visit_variant_mut.html" class="fn"
title="fn syn::visit_mut::visit_variant_mut">visit_variant_mut</a>

<a href="fn.visit_vis_restricted_mut.html" class="fn"
title="fn syn::visit_mut::visit_vis_restricted_mut">visit_vis_restricted_mut</a>

<a href="fn.visit_visibility_mut.html" class="fn"
title="fn syn::visit_mut::visit_visibility_mut">visit_visibility_mut</a>

<a href="fn.visit_where_clause_mut.html" class="fn"
title="fn syn::visit_mut::visit_where_clause_mut">visit_where_clause_mut</a>

<a href="fn.visit_where_predicate_mut.html" class="fn"
title="fn syn::visit_mut::visit_where_predicate_mut">visit_where_predicate_mut</a>

</div>

</div>
