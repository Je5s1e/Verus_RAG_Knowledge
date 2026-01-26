<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[syn](../index.html)::[visit](index.html)

</div>

# Trait <span class="trait">Visit</span> Copy item path

<span class="sub-heading"><a href="../../src/syn/gen/visit.rs.html#28-945" class="src">Source</a>
</span>

</div>

``` rust
pub trait Visit<'ast> {
Show 188 methods    // Provided methods
    fn visit_abi(&mut self, i: &'ast Abi) { ... }
    fn visit_angle_bracketed_generic_arguments(
        &mut self,
        i: &'ast AngleBracketedGenericArguments,
    ) { ... }
    fn visit_arm(&mut self, i: &'ast Arm) { ... }
    fn visit_assoc_const(&mut self, i: &'ast AssocConst) { ... }
    fn visit_assoc_type(&mut self, i: &'ast AssocType) { ... }
    fn visit_attr_style(&mut self, i: &'ast AttrStyle) { ... }
    fn visit_attribute(&mut self, i: &'ast Attribute) { ... }
    fn visit_bare_fn_arg(&mut self, i: &'ast BareFnArg) { ... }
    fn visit_bare_variadic(&mut self, i: &'ast BareVariadic) { ... }
    fn visit_bin_op(&mut self, i: &'ast BinOp) { ... }
    fn visit_block(&mut self, i: &'ast Block) { ... }
    fn visit_bound_lifetimes(&mut self, i: &'ast BoundLifetimes) { ... }
    fn visit_captured_param(&mut self, i: &'ast CapturedParam) { ... }
    fn visit_const_param(&mut self, i: &'ast ConstParam) { ... }
    fn visit_constraint(&mut self, i: &'ast Constraint) { ... }
    fn visit_data(&mut self, i: &'ast Data) { ... }
    fn visit_data_enum(&mut self, i: &'ast DataEnum) { ... }
    fn visit_data_struct(&mut self, i: &'ast DataStruct) { ... }
    fn visit_data_union(&mut self, i: &'ast DataUnion) { ... }
    fn visit_derive_input(&mut self, i: &'ast DeriveInput) { ... }
    fn visit_expr(&mut self, i: &'ast Expr) { ... }
    fn visit_expr_array(&mut self, i: &'ast ExprArray) { ... }
    fn visit_expr_assign(&mut self, i: &'ast ExprAssign) { ... }
    fn visit_expr_async(&mut self, i: &'ast ExprAsync) { ... }
    fn visit_expr_await(&mut self, i: &'ast ExprAwait) { ... }
    fn visit_expr_binary(&mut self, i: &'ast ExprBinary) { ... }
    fn visit_expr_block(&mut self, i: &'ast ExprBlock) { ... }
    fn visit_expr_break(&mut self, i: &'ast ExprBreak) { ... }
    fn visit_expr_call(&mut self, i: &'ast ExprCall) { ... }
    fn visit_expr_cast(&mut self, i: &'ast ExprCast) { ... }
    fn visit_expr_closure(&mut self, i: &'ast ExprClosure) { ... }
    fn visit_expr_const(&mut self, i: &'ast ExprConst) { ... }
    fn visit_expr_continue(&mut self, i: &'ast ExprContinue) { ... }
    fn visit_expr_field(&mut self, i: &'ast ExprField) { ... }
    fn visit_expr_for_loop(&mut self, i: &'ast ExprForLoop) { ... }
    fn visit_expr_group(&mut self, i: &'ast ExprGroup) { ... }
    fn visit_expr_if(&mut self, i: &'ast ExprIf) { ... }
    fn visit_expr_index(&mut self, i: &'ast ExprIndex) { ... }
    fn visit_expr_infer(&mut self, i: &'ast ExprInfer) { ... }
    fn visit_expr_let(&mut self, i: &'ast ExprLet) { ... }
    fn visit_expr_lit(&mut self, i: &'ast ExprLit) { ... }
    fn visit_expr_loop(&mut self, i: &'ast ExprLoop) { ... }
    fn visit_expr_macro(&mut self, i: &'ast ExprMacro) { ... }
    fn visit_expr_match(&mut self, i: &'ast ExprMatch) { ... }
    fn visit_expr_method_call(&mut self, i: &'ast ExprMethodCall) { ... }
    fn visit_expr_paren(&mut self, i: &'ast ExprParen) { ... }
    fn visit_expr_path(&mut self, i: &'ast ExprPath) { ... }
    fn visit_expr_range(&mut self, i: &'ast ExprRange) { ... }
    fn visit_expr_raw_addr(&mut self, i: &'ast ExprRawAddr) { ... }
    fn visit_expr_reference(&mut self, i: &'ast ExprReference) { ... }
    fn visit_expr_repeat(&mut self, i: &'ast ExprRepeat) { ... }
    fn visit_expr_return(&mut self, i: &'ast ExprReturn) { ... }
    fn visit_expr_struct(&mut self, i: &'ast ExprStruct) { ... }
    fn visit_expr_try(&mut self, i: &'ast ExprTry) { ... }
    fn visit_expr_try_block(&mut self, i: &'ast ExprTryBlock) { ... }
    fn visit_expr_tuple(&mut self, i: &'ast ExprTuple) { ... }
    fn visit_expr_unary(&mut self, i: &'ast ExprUnary) { ... }
    fn visit_expr_unsafe(&mut self, i: &'ast ExprUnsafe) { ... }
    fn visit_expr_while(&mut self, i: &'ast ExprWhile) { ... }
    fn visit_expr_yield(&mut self, i: &'ast ExprYield) { ... }
    fn visit_field(&mut self, i: &'ast Field) { ... }
    fn visit_field_mutability(&mut self, i: &'ast FieldMutability) { ... }
    fn visit_field_pat(&mut self, i: &'ast FieldPat) { ... }
    fn visit_field_value(&mut self, i: &'ast FieldValue) { ... }
    fn visit_fields(&mut self, i: &'ast Fields) { ... }
    fn visit_fields_named(&mut self, i: &'ast FieldsNamed) { ... }
    fn visit_fields_unnamed(&mut self, i: &'ast FieldsUnnamed) { ... }
    fn visit_file(&mut self, i: &'ast File) { ... }
    fn visit_fn_arg(&mut self, i: &'ast FnArg) { ... }
    fn visit_foreign_item(&mut self, i: &'ast ForeignItem) { ... }
    fn visit_foreign_item_fn(&mut self, i: &'ast ForeignItemFn) { ... }
    fn visit_foreign_item_macro(&mut self, i: &'ast ForeignItemMacro) { ... }
    fn visit_foreign_item_static(&mut self, i: &'ast ForeignItemStatic) { ... }
    fn visit_foreign_item_type(&mut self, i: &'ast ForeignItemType) { ... }
    fn visit_generic_argument(&mut self, i: &'ast GenericArgument) { ... }
    fn visit_generic_param(&mut self, i: &'ast GenericParam) { ... }
    fn visit_generics(&mut self, i: &'ast Generics) { ... }
    fn visit_ident(&mut self, i: &'ast Ident) { ... }
    fn visit_impl_item(&mut self, i: &'ast ImplItem) { ... }
    fn visit_impl_item_const(&mut self, i: &'ast ImplItemConst) { ... }
    fn visit_impl_item_fn(&mut self, i: &'ast ImplItemFn) { ... }
    fn visit_impl_item_macro(&mut self, i: &'ast ImplItemMacro) { ... }
    fn visit_impl_item_type(&mut self, i: &'ast ImplItemType) { ... }
    fn visit_impl_restriction(&mut self, i: &'ast ImplRestriction) { ... }
    fn visit_index(&mut self, i: &'ast Index) { ... }
    fn visit_item(&mut self, i: &'ast Item) { ... }
    fn visit_item_const(&mut self, i: &'ast ItemConst) { ... }
    fn visit_item_enum(&mut self, i: &'ast ItemEnum) { ... }
    fn visit_item_extern_crate(&mut self, i: &'ast ItemExternCrate) { ... }
    fn visit_item_fn(&mut self, i: &'ast ItemFn) { ... }
    fn visit_item_foreign_mod(&mut self, i: &'ast ItemForeignMod) { ... }
    fn visit_item_impl(&mut self, i: &'ast ItemImpl) { ... }
    fn visit_item_macro(&mut self, i: &'ast ItemMacro) { ... }
    fn visit_item_mod(&mut self, i: &'ast ItemMod) { ... }
    fn visit_item_static(&mut self, i: &'ast ItemStatic) { ... }
    fn visit_item_struct(&mut self, i: &'ast ItemStruct) { ... }
    fn visit_item_trait(&mut self, i: &'ast ItemTrait) { ... }
    fn visit_item_trait_alias(&mut self, i: &'ast ItemTraitAlias) { ... }
    fn visit_item_type(&mut self, i: &'ast ItemType) { ... }
    fn visit_item_union(&mut self, i: &'ast ItemUnion) { ... }
    fn visit_item_use(&mut self, i: &'ast ItemUse) { ... }
    fn visit_label(&mut self, i: &'ast Label) { ... }
    fn visit_lifetime(&mut self, i: &'ast Lifetime) { ... }
    fn visit_lifetime_param(&mut self, i: &'ast LifetimeParam) { ... }
    fn visit_lit(&mut self, i: &'ast Lit) { ... }
    fn visit_lit_bool(&mut self, i: &'ast LitBool) { ... }
    fn visit_lit_byte(&mut self, i: &'ast LitByte) { ... }
    fn visit_lit_byte_str(&mut self, i: &'ast LitByteStr) { ... }
    fn visit_lit_cstr(&mut self, i: &'ast LitCStr) { ... }
    fn visit_lit_char(&mut self, i: &'ast LitChar) { ... }
    fn visit_lit_float(&mut self, i: &'ast LitFloat) { ... }
    fn visit_lit_int(&mut self, i: &'ast LitInt) { ... }
    fn visit_lit_str(&mut self, i: &'ast LitStr) { ... }
    fn visit_local(&mut self, i: &'ast Local) { ... }
    fn visit_local_init(&mut self, i: &'ast LocalInit) { ... }
    fn visit_macro(&mut self, i: &'ast Macro) { ... }
    fn visit_macro_delimiter(&mut self, i: &'ast MacroDelimiter) { ... }
    fn visit_member(&mut self, i: &'ast Member) { ... }
    fn visit_meta(&mut self, i: &'ast Meta) { ... }
    fn visit_meta_list(&mut self, i: &'ast MetaList) { ... }
    fn visit_meta_name_value(&mut self, i: &'ast MetaNameValue) { ... }
    fn visit_parenthesized_generic_arguments(
        &mut self,
        i: &'ast ParenthesizedGenericArguments,
    ) { ... }
    fn visit_pat(&mut self, i: &'ast Pat) { ... }
    fn visit_pat_ident(&mut self, i: &'ast PatIdent) { ... }
    fn visit_pat_or(&mut self, i: &'ast PatOr) { ... }
    fn visit_pat_paren(&mut self, i: &'ast PatParen) { ... }
    fn visit_pat_reference(&mut self, i: &'ast PatReference) { ... }
    fn visit_pat_rest(&mut self, i: &'ast PatRest) { ... }
    fn visit_pat_slice(&mut self, i: &'ast PatSlice) { ... }
    fn visit_pat_struct(&mut self, i: &'ast PatStruct) { ... }
    fn visit_pat_tuple(&mut self, i: &'ast PatTuple) { ... }
    fn visit_pat_tuple_struct(&mut self, i: &'ast PatTupleStruct) { ... }
    fn visit_pat_type(&mut self, i: &'ast PatType) { ... }
    fn visit_pat_wild(&mut self, i: &'ast PatWild) { ... }
    fn visit_path(&mut self, i: &'ast Path) { ... }
    fn visit_path_arguments(&mut self, i: &'ast PathArguments) { ... }
    fn visit_path_segment(&mut self, i: &'ast PathSegment) { ... }
    fn visit_pointer_mutability(&mut self, i: &'ast PointerMutability) { ... }
    fn visit_precise_capture(&mut self, i: &'ast PreciseCapture) { ... }
    fn visit_predicate_lifetime(&mut self, i: &'ast PredicateLifetime) { ... }
    fn visit_predicate_type(&mut self, i: &'ast PredicateType) { ... }
    fn visit_qself(&mut self, i: &'ast QSelf) { ... }
    fn visit_range_limits(&mut self, i: &'ast RangeLimits) { ... }
    fn visit_receiver(&mut self, i: &'ast Receiver) { ... }
    fn visit_return_type(&mut self, i: &'ast ReturnType) { ... }
    fn visit_signature(&mut self, i: &'ast Signature) { ... }
    fn visit_span(&mut self, i: &Span) { ... }
    fn visit_static_mutability(&mut self, i: &'ast StaticMutability) { ... }
    fn visit_stmt(&mut self, i: &'ast Stmt) { ... }
    fn visit_stmt_macro(&mut self, i: &'ast StmtMacro) { ... }
    fn visit_token_stream(&mut self, i: &'ast TokenStream) { ... }
    fn visit_trait_bound(&mut self, i: &'ast TraitBound) { ... }
    fn visit_trait_bound_modifier(&mut self, i: &'ast TraitBoundModifier) { ... }
    fn visit_trait_item(&mut self, i: &'ast TraitItem) { ... }
    fn visit_trait_item_const(&mut self, i: &'ast TraitItemConst) { ... }
    fn visit_trait_item_fn(&mut self, i: &'ast TraitItemFn) { ... }
    fn visit_trait_item_macro(&mut self, i: &'ast TraitItemMacro) { ... }
    fn visit_trait_item_type(&mut self, i: &'ast TraitItemType) { ... }
    fn visit_type(&mut self, i: &'ast Type) { ... }
    fn visit_type_array(&mut self, i: &'ast TypeArray) { ... }
    fn visit_type_bare_fn(&mut self, i: &'ast TypeBareFn) { ... }
    fn visit_type_group(&mut self, i: &'ast TypeGroup) { ... }
    fn visit_type_impl_trait(&mut self, i: &'ast TypeImplTrait) { ... }
    fn visit_type_infer(&mut self, i: &'ast TypeInfer) { ... }
    fn visit_type_macro(&mut self, i: &'ast TypeMacro) { ... }
    fn visit_type_never(&mut self, i: &'ast TypeNever) { ... }
    fn visit_type_param(&mut self, i: &'ast TypeParam) { ... }
    fn visit_type_param_bound(&mut self, i: &'ast TypeParamBound) { ... }
    fn visit_type_paren(&mut self, i: &'ast TypeParen) { ... }
    fn visit_type_path(&mut self, i: &'ast TypePath) { ... }
    fn visit_type_ptr(&mut self, i: &'ast TypePtr) { ... }
    fn visit_type_reference(&mut self, i: &'ast TypeReference) { ... }
    fn visit_type_slice(&mut self, i: &'ast TypeSlice) { ... }
    fn visit_type_trait_object(&mut self, i: &'ast TypeTraitObject) { ... }
    fn visit_type_tuple(&mut self, i: &'ast TypeTuple) { ... }
    fn visit_un_op(&mut self, i: &'ast UnOp) { ... }
    fn visit_use_glob(&mut self, i: &'ast UseGlob) { ... }
    fn visit_use_group(&mut self, i: &'ast UseGroup) { ... }
    fn visit_use_name(&mut self, i: &'ast UseName) { ... }
    fn visit_use_path(&mut self, i: &'ast UsePath) { ... }
    fn visit_use_rename(&mut self, i: &'ast UseRename) { ... }
    fn visit_use_tree(&mut self, i: &'ast UseTree) { ... }
    fn visit_variadic(&mut self, i: &'ast Variadic) { ... }
    fn visit_variant(&mut self, i: &'ast Variant) { ... }
    fn visit_vis_restricted(&mut self, i: &'ast VisRestricted) { ... }
    fn visit_visibility(&mut self, i: &'ast Visibility) { ... }
    fn visit_where_clause(&mut self, i: &'ast WhereClause) { ... }
    fn visit_where_predicate(&mut self, i: &'ast WherePredicate) { ... }
}
```

Expand description

<div class="docblock">

Syntax tree traversal to walk a shared borrow of a syntax tree.

See the [module documentation](index.html "mod syn::visit") for details.

</div>

## Provided Methods<a href="#provided-methods" class="anchor">§</a>

<div class="methods">

<div id="method.visit_abi" class="section method">

<a href="../../src/syn/gen/visit.rs.html#31-33"
class="src rightside">Source</a>

#### fn <a href="#method.visit_abi" class="fn">visit_abi</a>(&mut self, i: &'ast <a href="../struct.Abi.html" class="struct"
title="struct syn::Abi">Abi</a>)

</div>

<div id="method.visit_angle_bracketed_generic_arguments"
class="section method">

<a href="../../src/syn/gen/visit.rs.html#36-41"
class="src rightside">Source</a>

#### fn <a href="#method.visit_angle_bracketed_generic_arguments"
class="fn">visit_angle_bracketed_generic_arguments</a>( &mut self, i: &'ast <a href="../struct.AngleBracketedGenericArguments.html" class="struct"
title="struct syn::AngleBracketedGenericArguments">AngleBracketedGenericArguments</a>, )

</div>

<div id="method.visit_arm" class="section method">

<a href="../../src/syn/gen/visit.rs.html#44-46"
class="src rightside">Source</a>

#### fn <a href="#method.visit_arm" class="fn">visit_arm</a>(&mut self, i: &'ast <a href="../struct.Arm.html" class="struct"
title="struct syn::Arm">Arm</a>)

</div>

<div id="method.visit_assoc_const" class="section method">

<a href="../../src/syn/gen/visit.rs.html#49-51"
class="src rightside">Source</a>

#### fn <a href="#method.visit_assoc_const" class="fn">visit_assoc_const</a>(&mut self, i: &'ast <a href="../struct.AssocConst.html" class="struct"
title="struct syn::AssocConst">AssocConst</a>)

</div>

<div id="method.visit_assoc_type" class="section method">

<a href="../../src/syn/gen/visit.rs.html#54-56"
class="src rightside">Source</a>

#### fn <a href="#method.visit_assoc_type" class="fn">visit_assoc_type</a>(&mut self, i: &'ast <a href="../struct.AssocType.html" class="struct"
title="struct syn::AssocType">AssocType</a>)

</div>

<div id="method.visit_attr_style" class="section method">

<a href="../../src/syn/gen/visit.rs.html#59-61"
class="src rightside">Source</a>

#### fn <a href="#method.visit_attr_style" class="fn">visit_attr_style</a>(&mut self, i: &'ast <a href="../enum.AttrStyle.html" class="enum"
title="enum syn::AttrStyle">AttrStyle</a>)

</div>

<div id="method.visit_attribute" class="section method">

<a href="../../src/syn/gen/visit.rs.html#64-66"
class="src rightside">Source</a>

#### fn <a href="#method.visit_attribute" class="fn">visit_attribute</a>(&mut self, i: &'ast <a href="../struct.Attribute.html" class="struct"
title="struct syn::Attribute">Attribute</a>)

</div>

<div id="method.visit_bare_fn_arg" class="section method">

<a href="../../src/syn/gen/visit.rs.html#69-71"
class="src rightside">Source</a>

#### fn <a href="#method.visit_bare_fn_arg" class="fn">visit_bare_fn_arg</a>(&mut self, i: &'ast <a href="../struct.BareFnArg.html" class="struct"
title="struct syn::BareFnArg">BareFnArg</a>)

</div>

<div id="method.visit_bare_variadic" class="section method">

<a href="../../src/syn/gen/visit.rs.html#74-76"
class="src rightside">Source</a>

#### fn <a href="#method.visit_bare_variadic" class="fn">visit_bare_variadic</a>(&mut self, i: &'ast <a href="../struct.BareVariadic.html" class="struct"
title="struct syn::BareVariadic">BareVariadic</a>)

</div>

<div id="method.visit_bin_op" class="section method">

<a href="../../src/syn/gen/visit.rs.html#79-81"
class="src rightside">Source</a>

#### fn <a href="#method.visit_bin_op" class="fn">visit_bin_op</a>(&mut self, i: &'ast <a href="../enum.BinOp.html" class="enum"
title="enum syn::BinOp">BinOp</a>)

</div>

<div id="method.visit_block" class="section method">

<a href="../../src/syn/gen/visit.rs.html#84-86"
class="src rightside">Source</a>

#### fn <a href="#method.visit_block" class="fn">visit_block</a>(&mut self, i: &'ast <a href="../struct.Block.html" class="struct"
title="struct syn::Block">Block</a>)

</div>

<div id="method.visit_bound_lifetimes" class="section method">

<a href="../../src/syn/gen/visit.rs.html#89-91"
class="src rightside">Source</a>

#### fn <a href="#method.visit_bound_lifetimes"
class="fn">visit_bound_lifetimes</a>(&mut self, i: &'ast <a href="../struct.BoundLifetimes.html" class="struct"
title="struct syn::BoundLifetimes">BoundLifetimes</a>)

</div>

<div id="method.visit_captured_param" class="section method">

<a href="../../src/syn/gen/visit.rs.html#94-96"
class="src rightside">Source</a>

#### fn <a href="#method.visit_captured_param"
class="fn">visit_captured_param</a>(&mut self, i: &'ast <a href="../enum.CapturedParam.html" class="enum"
title="enum syn::CapturedParam">CapturedParam</a>)

</div>

<div id="method.visit_const_param" class="section method">

<a href="../../src/syn/gen/visit.rs.html#99-101"
class="src rightside">Source</a>

#### fn <a href="#method.visit_const_param" class="fn">visit_const_param</a>(&mut self, i: &'ast <a href="../struct.ConstParam.html" class="struct"
title="struct syn::ConstParam">ConstParam</a>)

</div>

<div id="method.visit_constraint" class="section method">

<a href="../../src/syn/gen/visit.rs.html#104-106"
class="src rightside">Source</a>

#### fn <a href="#method.visit_constraint" class="fn">visit_constraint</a>(&mut self, i: &'ast <a href="../struct.Constraint.html" class="struct"
title="struct syn::Constraint">Constraint</a>)

</div>

<div id="method.visit_data" class="section method">

<a href="../../src/syn/gen/visit.rs.html#109-111"
class="src rightside">Source</a>

#### fn <a href="#method.visit_data" class="fn">visit_data</a>(&mut self, i: &'ast <a href="../enum.Data.html" class="enum" title="enum syn::Data">Data</a>)

</div>

<div id="method.visit_data_enum" class="section method">

<a href="../../src/syn/gen/visit.rs.html#114-116"
class="src rightside">Source</a>

#### fn <a href="#method.visit_data_enum" class="fn">visit_data_enum</a>(&mut self, i: &'ast <a href="../struct.DataEnum.html" class="struct"
title="struct syn::DataEnum">DataEnum</a>)

</div>

<div id="method.visit_data_struct" class="section method">

<a href="../../src/syn/gen/visit.rs.html#119-121"
class="src rightside">Source</a>

#### fn <a href="#method.visit_data_struct" class="fn">visit_data_struct</a>(&mut self, i: &'ast <a href="../struct.DataStruct.html" class="struct"
title="struct syn::DataStruct">DataStruct</a>)

</div>

<div id="method.visit_data_union" class="section method">

<a href="../../src/syn/gen/visit.rs.html#124-126"
class="src rightside">Source</a>

#### fn <a href="#method.visit_data_union" class="fn">visit_data_union</a>(&mut self, i: &'ast <a href="../struct.DataUnion.html" class="struct"
title="struct syn::DataUnion">DataUnion</a>)

</div>

<div id="method.visit_derive_input" class="section method">

<a href="../../src/syn/gen/visit.rs.html#129-131"
class="src rightside">Source</a>

#### fn <a href="#method.visit_derive_input" class="fn">visit_derive_input</a>(&mut self, i: &'ast <a href="../struct.DeriveInput.html" class="struct"
title="struct syn::DeriveInput">DeriveInput</a>)

</div>

<div id="method.visit_expr" class="section method">

<a href="../../src/syn/gen/visit.rs.html#134-136"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr" class="fn">visit_expr</a>(&mut self, i: &'ast <a href="../enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>)

</div>

<div id="method.visit_expr_array" class="section method">

<a href="../../src/syn/gen/visit.rs.html#139-141"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_array" class="fn">visit_expr_array</a>(&mut self, i: &'ast <a href="../struct.ExprArray.html" class="struct"
title="struct syn::ExprArray">ExprArray</a>)

</div>

<div id="method.visit_expr_assign" class="section method">

<a href="../../src/syn/gen/visit.rs.html#144-146"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_assign" class="fn">visit_expr_assign</a>(&mut self, i: &'ast <a href="../struct.ExprAssign.html" class="struct"
title="struct syn::ExprAssign">ExprAssign</a>)

</div>

<div id="method.visit_expr_async" class="section method">

<a href="../../src/syn/gen/visit.rs.html#149-151"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_async" class="fn">visit_expr_async</a>(&mut self, i: &'ast <a href="../struct.ExprAsync.html" class="struct"
title="struct syn::ExprAsync">ExprAsync</a>)

</div>

<div id="method.visit_expr_await" class="section method">

<a href="../../src/syn/gen/visit.rs.html#154-156"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_await" class="fn">visit_expr_await</a>(&mut self, i: &'ast <a href="../struct.ExprAwait.html" class="struct"
title="struct syn::ExprAwait">ExprAwait</a>)

</div>

<div id="method.visit_expr_binary" class="section method">

<a href="../../src/syn/gen/visit.rs.html#159-161"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_binary" class="fn">visit_expr_binary</a>(&mut self, i: &'ast <a href="../struct.ExprBinary.html" class="struct"
title="struct syn::ExprBinary">ExprBinary</a>)

</div>

<div id="method.visit_expr_block" class="section method">

<a href="../../src/syn/gen/visit.rs.html#164-166"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_block" class="fn">visit_expr_block</a>(&mut self, i: &'ast <a href="../struct.ExprBlock.html" class="struct"
title="struct syn::ExprBlock">ExprBlock</a>)

</div>

<div id="method.visit_expr_break" class="section method">

<a href="../../src/syn/gen/visit.rs.html#169-171"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_break" class="fn">visit_expr_break</a>(&mut self, i: &'ast <a href="../struct.ExprBreak.html" class="struct"
title="struct syn::ExprBreak">ExprBreak</a>)

</div>

<div id="method.visit_expr_call" class="section method">

<a href="../../src/syn/gen/visit.rs.html#174-176"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_call" class="fn">visit_expr_call</a>(&mut self, i: &'ast <a href="../struct.ExprCall.html" class="struct"
title="struct syn::ExprCall">ExprCall</a>)

</div>

<div id="method.visit_expr_cast" class="section method">

<a href="../../src/syn/gen/visit.rs.html#179-181"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_cast" class="fn">visit_expr_cast</a>(&mut self, i: &'ast <a href="../struct.ExprCast.html" class="struct"
title="struct syn::ExprCast">ExprCast</a>)

</div>

<div id="method.visit_expr_closure" class="section method">

<a href="../../src/syn/gen/visit.rs.html#184-186"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_closure" class="fn">visit_expr_closure</a>(&mut self, i: &'ast <a href="../struct.ExprClosure.html" class="struct"
title="struct syn::ExprClosure">ExprClosure</a>)

</div>

<div id="method.visit_expr_const" class="section method">

<a href="../../src/syn/gen/visit.rs.html#189-191"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_const" class="fn">visit_expr_const</a>(&mut self, i: &'ast <a href="../struct.ExprConst.html" class="struct"
title="struct syn::ExprConst">ExprConst</a>)

</div>

<div id="method.visit_expr_continue" class="section method">

<a href="../../src/syn/gen/visit.rs.html#194-196"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_continue" class="fn">visit_expr_continue</a>(&mut self, i: &'ast <a href="../struct.ExprContinue.html" class="struct"
title="struct syn::ExprContinue">ExprContinue</a>)

</div>

<div id="method.visit_expr_field" class="section method">

<a href="../../src/syn/gen/visit.rs.html#199-201"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_field" class="fn">visit_expr_field</a>(&mut self, i: &'ast <a href="../struct.ExprField.html" class="struct"
title="struct syn::ExprField">ExprField</a>)

</div>

<div id="method.visit_expr_for_loop" class="section method">

<a href="../../src/syn/gen/visit.rs.html#204-206"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_for_loop" class="fn">visit_expr_for_loop</a>(&mut self, i: &'ast <a href="../struct.ExprForLoop.html" class="struct"
title="struct syn::ExprForLoop">ExprForLoop</a>)

</div>

<div id="method.visit_expr_group" class="section method">

<a href="../../src/syn/gen/visit.rs.html#209-211"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_group" class="fn">visit_expr_group</a>(&mut self, i: &'ast <a href="../struct.ExprGroup.html" class="struct"
title="struct syn::ExprGroup">ExprGroup</a>)

</div>

<div id="method.visit_expr_if" class="section method">

<a href="../../src/syn/gen/visit.rs.html#214-216"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_if" class="fn">visit_expr_if</a>(&mut self, i: &'ast <a href="../struct.ExprIf.html" class="struct"
title="struct syn::ExprIf">ExprIf</a>)

</div>

<div id="method.visit_expr_index" class="section method">

<a href="../../src/syn/gen/visit.rs.html#219-221"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_index" class="fn">visit_expr_index</a>(&mut self, i: &'ast <a href="../struct.ExprIndex.html" class="struct"
title="struct syn::ExprIndex">ExprIndex</a>)

</div>

<div id="method.visit_expr_infer" class="section method">

<a href="../../src/syn/gen/visit.rs.html#224-226"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_infer" class="fn">visit_expr_infer</a>(&mut self, i: &'ast <a href="../struct.ExprInfer.html" class="struct"
title="struct syn::ExprInfer">ExprInfer</a>)

</div>

<div id="method.visit_expr_let" class="section method">

<a href="../../src/syn/gen/visit.rs.html#229-231"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_let" class="fn">visit_expr_let</a>(&mut self, i: &'ast <a href="../struct.ExprLet.html" class="struct"
title="struct syn::ExprLet">ExprLet</a>)

</div>

<div id="method.visit_expr_lit" class="section method">

<a href="../../src/syn/gen/visit.rs.html#234-236"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_lit" class="fn">visit_expr_lit</a>(&mut self, i: &'ast <a href="../struct.ExprLit.html" class="struct"
title="struct syn::ExprLit">ExprLit</a>)

</div>

<div id="method.visit_expr_loop" class="section method">

<a href="../../src/syn/gen/visit.rs.html#239-241"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_loop" class="fn">visit_expr_loop</a>(&mut self, i: &'ast <a href="../struct.ExprLoop.html" class="struct"
title="struct syn::ExprLoop">ExprLoop</a>)

</div>

<div id="method.visit_expr_macro" class="section method">

<a href="../../src/syn/gen/visit.rs.html#244-246"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_macro" class="fn">visit_expr_macro</a>(&mut self, i: &'ast <a href="../struct.ExprMacro.html" class="struct"
title="struct syn::ExprMacro">ExprMacro</a>)

</div>

<div id="method.visit_expr_match" class="section method">

<a href="../../src/syn/gen/visit.rs.html#249-251"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_match" class="fn">visit_expr_match</a>(&mut self, i: &'ast <a href="../struct.ExprMatch.html" class="struct"
title="struct syn::ExprMatch">ExprMatch</a>)

</div>

<div id="method.visit_expr_method_call" class="section method">

<a href="../../src/syn/gen/visit.rs.html#254-256"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_method_call"
class="fn">visit_expr_method_call</a>(&mut self, i: &'ast <a href="../struct.ExprMethodCall.html" class="struct"
title="struct syn::ExprMethodCall">ExprMethodCall</a>)

</div>

<div id="method.visit_expr_paren" class="section method">

<a href="../../src/syn/gen/visit.rs.html#259-261"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_paren" class="fn">visit_expr_paren</a>(&mut self, i: &'ast <a href="../struct.ExprParen.html" class="struct"
title="struct syn::ExprParen">ExprParen</a>)

</div>

<div id="method.visit_expr_path" class="section method">

<a href="../../src/syn/gen/visit.rs.html#264-266"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_path" class="fn">visit_expr_path</a>(&mut self, i: &'ast <a href="../struct.ExprPath.html" class="struct"
title="struct syn::ExprPath">ExprPath</a>)

</div>

<div id="method.visit_expr_range" class="section method">

<a href="../../src/syn/gen/visit.rs.html#269-271"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_range" class="fn">visit_expr_range</a>(&mut self, i: &'ast <a href="../struct.ExprRange.html" class="struct"
title="struct syn::ExprRange">ExprRange</a>)

</div>

<div id="method.visit_expr_raw_addr" class="section method">

<a href="../../src/syn/gen/visit.rs.html#274-276"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_raw_addr" class="fn">visit_expr_raw_addr</a>(&mut self, i: &'ast <a href="../struct.ExprRawAddr.html" class="struct"
title="struct syn::ExprRawAddr">ExprRawAddr</a>)

</div>

<div id="method.visit_expr_reference" class="section method">

<a href="../../src/syn/gen/visit.rs.html#279-281"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_reference"
class="fn">visit_expr_reference</a>(&mut self, i: &'ast <a href="../struct.ExprReference.html" class="struct"
title="struct syn::ExprReference">ExprReference</a>)

</div>

<div id="method.visit_expr_repeat" class="section method">

<a href="../../src/syn/gen/visit.rs.html#284-286"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_repeat" class="fn">visit_expr_repeat</a>(&mut self, i: &'ast <a href="../struct.ExprRepeat.html" class="struct"
title="struct syn::ExprRepeat">ExprRepeat</a>)

</div>

<div id="method.visit_expr_return" class="section method">

<a href="../../src/syn/gen/visit.rs.html#289-291"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_return" class="fn">visit_expr_return</a>(&mut self, i: &'ast <a href="../struct.ExprReturn.html" class="struct"
title="struct syn::ExprReturn">ExprReturn</a>)

</div>

<div id="method.visit_expr_struct" class="section method">

<a href="../../src/syn/gen/visit.rs.html#294-296"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_struct" class="fn">visit_expr_struct</a>(&mut self, i: &'ast <a href="../struct.ExprStruct.html" class="struct"
title="struct syn::ExprStruct">ExprStruct</a>)

</div>

<div id="method.visit_expr_try" class="section method">

<a href="../../src/syn/gen/visit.rs.html#299-301"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_try" class="fn">visit_expr_try</a>(&mut self, i: &'ast <a href="../struct.ExprTry.html" class="struct"
title="struct syn::ExprTry">ExprTry</a>)

</div>

<div id="method.visit_expr_try_block" class="section method">

<a href="../../src/syn/gen/visit.rs.html#304-306"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_try_block"
class="fn">visit_expr_try_block</a>(&mut self, i: &'ast <a href="../struct.ExprTryBlock.html" class="struct"
title="struct syn::ExprTryBlock">ExprTryBlock</a>)

</div>

<div id="method.visit_expr_tuple" class="section method">

<a href="../../src/syn/gen/visit.rs.html#309-311"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_tuple" class="fn">visit_expr_tuple</a>(&mut self, i: &'ast <a href="../struct.ExprTuple.html" class="struct"
title="struct syn::ExprTuple">ExprTuple</a>)

</div>

<div id="method.visit_expr_unary" class="section method">

<a href="../../src/syn/gen/visit.rs.html#314-316"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_unary" class="fn">visit_expr_unary</a>(&mut self, i: &'ast <a href="../struct.ExprUnary.html" class="struct"
title="struct syn::ExprUnary">ExprUnary</a>)

</div>

<div id="method.visit_expr_unsafe" class="section method">

<a href="../../src/syn/gen/visit.rs.html#319-321"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_unsafe" class="fn">visit_expr_unsafe</a>(&mut self, i: &'ast <a href="../struct.ExprUnsafe.html" class="struct"
title="struct syn::ExprUnsafe">ExprUnsafe</a>)

</div>

<div id="method.visit_expr_while" class="section method">

<a href="../../src/syn/gen/visit.rs.html#324-326"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_while" class="fn">visit_expr_while</a>(&mut self, i: &'ast <a href="../struct.ExprWhile.html" class="struct"
title="struct syn::ExprWhile">ExprWhile</a>)

</div>

<div id="method.visit_expr_yield" class="section method">

<a href="../../src/syn/gen/visit.rs.html#329-331"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_yield" class="fn">visit_expr_yield</a>(&mut self, i: &'ast <a href="../struct.ExprYield.html" class="struct"
title="struct syn::ExprYield">ExprYield</a>)

</div>

<div id="method.visit_field" class="section method">

<a href="../../src/syn/gen/visit.rs.html#334-336"
class="src rightside">Source</a>

#### fn <a href="#method.visit_field" class="fn">visit_field</a>(&mut self, i: &'ast <a href="../struct.Field.html" class="struct"
title="struct syn::Field">Field</a>)

</div>

<div id="method.visit_field_mutability" class="section method">

<a href="../../src/syn/gen/visit.rs.html#339-341"
class="src rightside">Source</a>

#### fn <a href="#method.visit_field_mutability"
class="fn">visit_field_mutability</a>(&mut self, i: &'ast <a href="../enum.FieldMutability.html" class="enum"
title="enum syn::FieldMutability">FieldMutability</a>)

</div>

<div id="method.visit_field_pat" class="section method">

<a href="../../src/syn/gen/visit.rs.html#344-346"
class="src rightside">Source</a>

#### fn <a href="#method.visit_field_pat" class="fn">visit_field_pat</a>(&mut self, i: &'ast <a href="../struct.FieldPat.html" class="struct"
title="struct syn::FieldPat">FieldPat</a>)

</div>

<div id="method.visit_field_value" class="section method">

<a href="../../src/syn/gen/visit.rs.html#349-351"
class="src rightside">Source</a>

#### fn <a href="#method.visit_field_value" class="fn">visit_field_value</a>(&mut self, i: &'ast <a href="../struct.FieldValue.html" class="struct"
title="struct syn::FieldValue">FieldValue</a>)

</div>

<div id="method.visit_fields" class="section method">

<a href="../../src/syn/gen/visit.rs.html#354-356"
class="src rightside">Source</a>

#### fn <a href="#method.visit_fields" class="fn">visit_fields</a>(&mut self, i: &'ast <a href="../enum.Fields.html" class="enum"
title="enum syn::Fields">Fields</a>)

</div>

<div id="method.visit_fields_named" class="section method">

<a href="../../src/syn/gen/visit.rs.html#359-361"
class="src rightside">Source</a>

#### fn <a href="#method.visit_fields_named" class="fn">visit_fields_named</a>(&mut self, i: &'ast <a href="../struct.FieldsNamed.html" class="struct"
title="struct syn::FieldsNamed">FieldsNamed</a>)

</div>

<div id="method.visit_fields_unnamed" class="section method">

<a href="../../src/syn/gen/visit.rs.html#364-366"
class="src rightside">Source</a>

#### fn <a href="#method.visit_fields_unnamed"
class="fn">visit_fields_unnamed</a>(&mut self, i: &'ast <a href="../struct.FieldsUnnamed.html" class="struct"
title="struct syn::FieldsUnnamed">FieldsUnnamed</a>)

</div>

<div id="method.visit_file" class="section method">

<a href="../../src/syn/gen/visit.rs.html#369-371"
class="src rightside">Source</a>

#### fn <a href="#method.visit_file" class="fn">visit_file</a>(&mut self, i: &'ast <a href="../struct.File.html" class="struct"
title="struct syn::File">File</a>)

</div>

<div id="method.visit_fn_arg" class="section method">

<a href="../../src/syn/gen/visit.rs.html#374-376"
class="src rightside">Source</a>

#### fn <a href="#method.visit_fn_arg" class="fn">visit_fn_arg</a>(&mut self, i: &'ast <a href="../enum.FnArg.html" class="enum"
title="enum syn::FnArg">FnArg</a>)

</div>

<div id="method.visit_foreign_item" class="section method">

<a href="../../src/syn/gen/visit.rs.html#379-381"
class="src rightside">Source</a>

#### fn <a href="#method.visit_foreign_item" class="fn">visit_foreign_item</a>(&mut self, i: &'ast <a href="../enum.ForeignItem.html" class="enum"
title="enum syn::ForeignItem">ForeignItem</a>)

</div>

<div id="method.visit_foreign_item_fn" class="section method">

<a href="../../src/syn/gen/visit.rs.html#384-386"
class="src rightside">Source</a>

#### fn <a href="#method.visit_foreign_item_fn"
class="fn">visit_foreign_item_fn</a>(&mut self, i: &'ast <a href="../struct.ForeignItemFn.html" class="struct"
title="struct syn::ForeignItemFn">ForeignItemFn</a>)

</div>

<div id="method.visit_foreign_item_macro" class="section method">

<a href="../../src/syn/gen/visit.rs.html#389-391"
class="src rightside">Source</a>

#### fn <a href="#method.visit_foreign_item_macro"
class="fn">visit_foreign_item_macro</a>(&mut self, i: &'ast <a href="../struct.ForeignItemMacro.html" class="struct"
title="struct syn::ForeignItemMacro">ForeignItemMacro</a>)

</div>

<div id="method.visit_foreign_item_static" class="section method">

<a href="../../src/syn/gen/visit.rs.html#394-396"
class="src rightside">Source</a>

#### fn <a href="#method.visit_foreign_item_static"
class="fn">visit_foreign_item_static</a>(&mut self, i: &'ast <a href="../struct.ForeignItemStatic.html" class="struct"
title="struct syn::ForeignItemStatic">ForeignItemStatic</a>)

</div>

<div id="method.visit_foreign_item_type" class="section method">

<a href="../../src/syn/gen/visit.rs.html#399-401"
class="src rightside">Source</a>

#### fn <a href="#method.visit_foreign_item_type"
class="fn">visit_foreign_item_type</a>(&mut self, i: &'ast <a href="../struct.ForeignItemType.html" class="struct"
title="struct syn::ForeignItemType">ForeignItemType</a>)

</div>

<div id="method.visit_generic_argument" class="section method">

<a href="../../src/syn/gen/visit.rs.html#404-406"
class="src rightside">Source</a>

#### fn <a href="#method.visit_generic_argument"
class="fn">visit_generic_argument</a>(&mut self, i: &'ast <a href="../enum.GenericArgument.html" class="enum"
title="enum syn::GenericArgument">GenericArgument</a>)

</div>

<div id="method.visit_generic_param" class="section method">

<a href="../../src/syn/gen/visit.rs.html#409-411"
class="src rightside">Source</a>

#### fn <a href="#method.visit_generic_param" class="fn">visit_generic_param</a>(&mut self, i: &'ast <a href="../enum.GenericParam.html" class="enum"
title="enum syn::GenericParam">GenericParam</a>)

</div>

<div id="method.visit_generics" class="section method">

<a href="../../src/syn/gen/visit.rs.html#414-416"
class="src rightside">Source</a>

#### fn <a href="#method.visit_generics" class="fn">visit_generics</a>(&mut self, i: &'ast <a href="../struct.Generics.html" class="struct"
title="struct syn::Generics">Generics</a>)

</div>

<div id="method.visit_ident" class="section method">

<a href="../../src/syn/gen/visit.rs.html#417-419"
class="src rightside">Source</a>

#### fn <a href="#method.visit_ident" class="fn">visit_ident</a>(&mut self, i: &'ast <a href="../struct.Ident.html" class="struct"
title="struct syn::Ident">Ident</a>)

</div>

<div id="method.visit_impl_item" class="section method">

<a href="../../src/syn/gen/visit.rs.html#422-424"
class="src rightside">Source</a>

#### fn <a href="#method.visit_impl_item" class="fn">visit_impl_item</a>(&mut self, i: &'ast <a href="../enum.ImplItem.html" class="enum"
title="enum syn::ImplItem">ImplItem</a>)

</div>

<div id="method.visit_impl_item_const" class="section method">

<a href="../../src/syn/gen/visit.rs.html#427-429"
class="src rightside">Source</a>

#### fn <a href="#method.visit_impl_item_const"
class="fn">visit_impl_item_const</a>(&mut self, i: &'ast <a href="../struct.ImplItemConst.html" class="struct"
title="struct syn::ImplItemConst">ImplItemConst</a>)

</div>

<div id="method.visit_impl_item_fn" class="section method">

<a href="../../src/syn/gen/visit.rs.html#432-434"
class="src rightside">Source</a>

#### fn <a href="#method.visit_impl_item_fn" class="fn">visit_impl_item_fn</a>(&mut self, i: &'ast <a href="../struct.ImplItemFn.html" class="struct"
title="struct syn::ImplItemFn">ImplItemFn</a>)

</div>

<div id="method.visit_impl_item_macro" class="section method">

<a href="../../src/syn/gen/visit.rs.html#437-439"
class="src rightside">Source</a>

#### fn <a href="#method.visit_impl_item_macro"
class="fn">visit_impl_item_macro</a>(&mut self, i: &'ast <a href="../struct.ImplItemMacro.html" class="struct"
title="struct syn::ImplItemMacro">ImplItemMacro</a>)

</div>

<div id="method.visit_impl_item_type" class="section method">

<a href="../../src/syn/gen/visit.rs.html#442-444"
class="src rightside">Source</a>

#### fn <a href="#method.visit_impl_item_type"
class="fn">visit_impl_item_type</a>(&mut self, i: &'ast <a href="../struct.ImplItemType.html" class="struct"
title="struct syn::ImplItemType">ImplItemType</a>)

</div>

<div id="method.visit_impl_restriction" class="section method">

<a href="../../src/syn/gen/visit.rs.html#447-449"
class="src rightside">Source</a>

#### fn <a href="#method.visit_impl_restriction"
class="fn">visit_impl_restriction</a>(&mut self, i: &'ast <a href="../enum.ImplRestriction.html" class="enum"
title="enum syn::ImplRestriction">ImplRestriction</a>)

</div>

<div id="method.visit_index" class="section method">

<a href="../../src/syn/gen/visit.rs.html#452-454"
class="src rightside">Source</a>

#### fn <a href="#method.visit_index" class="fn">visit_index</a>(&mut self, i: &'ast <a href="../struct.Index.html" class="struct"
title="struct syn::Index">Index</a>)

</div>

<div id="method.visit_item" class="section method">

<a href="../../src/syn/gen/visit.rs.html#457-459"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item" class="fn">visit_item</a>(&mut self, i: &'ast <a href="../enum.Item.html" class="enum" title="enum syn::Item">Item</a>)

</div>

<div id="method.visit_item_const" class="section method">

<a href="../../src/syn/gen/visit.rs.html#462-464"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_const" class="fn">visit_item_const</a>(&mut self, i: &'ast <a href="../struct.ItemConst.html" class="struct"
title="struct syn::ItemConst">ItemConst</a>)

</div>

<div id="method.visit_item_enum" class="section method">

<a href="../../src/syn/gen/visit.rs.html#467-469"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_enum" class="fn">visit_item_enum</a>(&mut self, i: &'ast <a href="../struct.ItemEnum.html" class="struct"
title="struct syn::ItemEnum">ItemEnum</a>)

</div>

<div id="method.visit_item_extern_crate" class="section method">

<a href="../../src/syn/gen/visit.rs.html#472-474"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_extern_crate"
class="fn">visit_item_extern_crate</a>(&mut self, i: &'ast <a href="../struct.ItemExternCrate.html" class="struct"
title="struct syn::ItemExternCrate">ItemExternCrate</a>)

</div>

<div id="method.visit_item_fn" class="section method">

<a href="../../src/syn/gen/visit.rs.html#477-479"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_fn" class="fn">visit_item_fn</a>(&mut self, i: &'ast <a href="../struct.ItemFn.html" class="struct"
title="struct syn::ItemFn">ItemFn</a>)

</div>

<div id="method.visit_item_foreign_mod" class="section method">

<a href="../../src/syn/gen/visit.rs.html#482-484"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_foreign_mod"
class="fn">visit_item_foreign_mod</a>(&mut self, i: &'ast <a href="../struct.ItemForeignMod.html" class="struct"
title="struct syn::ItemForeignMod">ItemForeignMod</a>)

</div>

<div id="method.visit_item_impl" class="section method">

<a href="../../src/syn/gen/visit.rs.html#487-489"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_impl" class="fn">visit_item_impl</a>(&mut self, i: &'ast <a href="../struct.ItemImpl.html" class="struct"
title="struct syn::ItemImpl">ItemImpl</a>)

</div>

<div id="method.visit_item_macro" class="section method">

<a href="../../src/syn/gen/visit.rs.html#492-494"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_macro" class="fn">visit_item_macro</a>(&mut self, i: &'ast <a href="../struct.ItemMacro.html" class="struct"
title="struct syn::ItemMacro">ItemMacro</a>)

</div>

<div id="method.visit_item_mod" class="section method">

<a href="../../src/syn/gen/visit.rs.html#497-499"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_mod" class="fn">visit_item_mod</a>(&mut self, i: &'ast <a href="../struct.ItemMod.html" class="struct"
title="struct syn::ItemMod">ItemMod</a>)

</div>

<div id="method.visit_item_static" class="section method">

<a href="../../src/syn/gen/visit.rs.html#502-504"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_static" class="fn">visit_item_static</a>(&mut self, i: &'ast <a href="../struct.ItemStatic.html" class="struct"
title="struct syn::ItemStatic">ItemStatic</a>)

</div>

<div id="method.visit_item_struct" class="section method">

<a href="../../src/syn/gen/visit.rs.html#507-509"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_struct" class="fn">visit_item_struct</a>(&mut self, i: &'ast <a href="../struct.ItemStruct.html" class="struct"
title="struct syn::ItemStruct">ItemStruct</a>)

</div>

<div id="method.visit_item_trait" class="section method">

<a href="../../src/syn/gen/visit.rs.html#512-514"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_trait" class="fn">visit_item_trait</a>(&mut self, i: &'ast <a href="../struct.ItemTrait.html" class="struct"
title="struct syn::ItemTrait">ItemTrait</a>)

</div>

<div id="method.visit_item_trait_alias" class="section method">

<a href="../../src/syn/gen/visit.rs.html#517-519"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_trait_alias"
class="fn">visit_item_trait_alias</a>(&mut self, i: &'ast <a href="../struct.ItemTraitAlias.html" class="struct"
title="struct syn::ItemTraitAlias">ItemTraitAlias</a>)

</div>

<div id="method.visit_item_type" class="section method">

<a href="../../src/syn/gen/visit.rs.html#522-524"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_type" class="fn">visit_item_type</a>(&mut self, i: &'ast <a href="../struct.ItemType.html" class="struct"
title="struct syn::ItemType">ItemType</a>)

</div>

<div id="method.visit_item_union" class="section method">

<a href="../../src/syn/gen/visit.rs.html#527-529"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_union" class="fn">visit_item_union</a>(&mut self, i: &'ast <a href="../struct.ItemUnion.html" class="struct"
title="struct syn::ItemUnion">ItemUnion</a>)

</div>

<div id="method.visit_item_use" class="section method">

<a href="../../src/syn/gen/visit.rs.html#532-534"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_use" class="fn">visit_item_use</a>(&mut self, i: &'ast <a href="../struct.ItemUse.html" class="struct"
title="struct syn::ItemUse">ItemUse</a>)

</div>

<div id="method.visit_label" class="section method">

<a href="../../src/syn/gen/visit.rs.html#537-539"
class="src rightside">Source</a>

#### fn <a href="#method.visit_label" class="fn">visit_label</a>(&mut self, i: &'ast <a href="../struct.Label.html" class="struct"
title="struct syn::Label">Label</a>)

</div>

<div id="method.visit_lifetime" class="section method">

<a href="../../src/syn/gen/visit.rs.html#540-542"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lifetime" class="fn">visit_lifetime</a>(&mut self, i: &'ast <a href="../struct.Lifetime.html" class="struct"
title="struct syn::Lifetime">Lifetime</a>)

</div>

<div id="method.visit_lifetime_param" class="section method">

<a href="../../src/syn/gen/visit.rs.html#545-547"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lifetime_param"
class="fn">visit_lifetime_param</a>(&mut self, i: &'ast <a href="../struct.LifetimeParam.html" class="struct"
title="struct syn::LifetimeParam">LifetimeParam</a>)

</div>

<div id="method.visit_lit" class="section method">

<a href="../../src/syn/gen/visit.rs.html#548-550"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lit" class="fn">visit_lit</a>(&mut self, i: &'ast <a href="../enum.Lit.html" class="enum" title="enum syn::Lit">Lit</a>)

</div>

<div id="method.visit_lit_bool" class="section method">

<a href="../../src/syn/gen/visit.rs.html#551-553"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lit_bool" class="fn">visit_lit_bool</a>(&mut self, i: &'ast <a href="../struct.LitBool.html" class="struct"
title="struct syn::LitBool">LitBool</a>)

</div>

<div id="method.visit_lit_byte" class="section method">

<a href="../../src/syn/gen/visit.rs.html#554-556"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lit_byte" class="fn">visit_lit_byte</a>(&mut self, i: &'ast <a href="../struct.LitByte.html" class="struct"
title="struct syn::LitByte">LitByte</a>)

</div>

<div id="method.visit_lit_byte_str" class="section method">

<a href="../../src/syn/gen/visit.rs.html#557-559"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lit_byte_str" class="fn">visit_lit_byte_str</a>(&mut self, i: &'ast <a href="../struct.LitByteStr.html" class="struct"
title="struct syn::LitByteStr">LitByteStr</a>)

</div>

<div id="method.visit_lit_cstr" class="section method">

<a href="../../src/syn/gen/visit.rs.html#560-562"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lit_cstr" class="fn">visit_lit_cstr</a>(&mut self, i: &'ast <a href="../struct.LitCStr.html" class="struct"
title="struct syn::LitCStr">LitCStr</a>)

</div>

<div id="method.visit_lit_char" class="section method">

<a href="../../src/syn/gen/visit.rs.html#563-565"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lit_char" class="fn">visit_lit_char</a>(&mut self, i: &'ast <a href="../struct.LitChar.html" class="struct"
title="struct syn::LitChar">LitChar</a>)

</div>

<div id="method.visit_lit_float" class="section method">

<a href="../../src/syn/gen/visit.rs.html#566-568"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lit_float" class="fn">visit_lit_float</a>(&mut self, i: &'ast <a href="../struct.LitFloat.html" class="struct"
title="struct syn::LitFloat">LitFloat</a>)

</div>

<div id="method.visit_lit_int" class="section method">

<a href="../../src/syn/gen/visit.rs.html#569-571"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lit_int" class="fn">visit_lit_int</a>(&mut self, i: &'ast <a href="../struct.LitInt.html" class="struct"
title="struct syn::LitInt">LitInt</a>)

</div>

<div id="method.visit_lit_str" class="section method">

<a href="../../src/syn/gen/visit.rs.html#572-574"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lit_str" class="fn">visit_lit_str</a>(&mut self, i: &'ast <a href="../struct.LitStr.html" class="struct"
title="struct syn::LitStr">LitStr</a>)

</div>

<div id="method.visit_local" class="section method">

<a href="../../src/syn/gen/visit.rs.html#577-579"
class="src rightside">Source</a>

#### fn <a href="#method.visit_local" class="fn">visit_local</a>(&mut self, i: &'ast <a href="../struct.Local.html" class="struct"
title="struct syn::Local">Local</a>)

</div>

<div id="method.visit_local_init" class="section method">

<a href="../../src/syn/gen/visit.rs.html#582-584"
class="src rightside">Source</a>

#### fn <a href="#method.visit_local_init" class="fn">visit_local_init</a>(&mut self, i: &'ast <a href="../struct.LocalInit.html" class="struct"
title="struct syn::LocalInit">LocalInit</a>)

</div>

<div id="method.visit_macro" class="section method">

<a href="../../src/syn/gen/visit.rs.html#587-589"
class="src rightside">Source</a>

#### fn <a href="#method.visit_macro" class="fn">visit_macro</a>(&mut self, i: &'ast <a href="../struct.Macro.html" class="struct"
title="struct syn::Macro">Macro</a>)

</div>

<div id="method.visit_macro_delimiter" class="section method">

<a href="../../src/syn/gen/visit.rs.html#592-594"
class="src rightside">Source</a>

#### fn <a href="#method.visit_macro_delimiter"
class="fn">visit_macro_delimiter</a>(&mut self, i: &'ast <a href="../enum.MacroDelimiter.html" class="enum"
title="enum syn::MacroDelimiter">MacroDelimiter</a>)

</div>

<div id="method.visit_member" class="section method">

<a href="../../src/syn/gen/visit.rs.html#597-599"
class="src rightside">Source</a>

#### fn <a href="#method.visit_member" class="fn">visit_member</a>(&mut self, i: &'ast <a href="../enum.Member.html" class="enum"
title="enum syn::Member">Member</a>)

</div>

<div id="method.visit_meta" class="section method">

<a href="../../src/syn/gen/visit.rs.html#602-604"
class="src rightside">Source</a>

#### fn <a href="#method.visit_meta" class="fn">visit_meta</a>(&mut self, i: &'ast <a href="../enum.Meta.html" class="enum" title="enum syn::Meta">Meta</a>)

</div>

<div id="method.visit_meta_list" class="section method">

<a href="../../src/syn/gen/visit.rs.html#607-609"
class="src rightside">Source</a>

#### fn <a href="#method.visit_meta_list" class="fn">visit_meta_list</a>(&mut self, i: &'ast <a href="../struct.MetaList.html" class="struct"
title="struct syn::MetaList">MetaList</a>)

</div>

<div id="method.visit_meta_name_value" class="section method">

<a href="../../src/syn/gen/visit.rs.html#612-614"
class="src rightside">Source</a>

#### fn <a href="#method.visit_meta_name_value"
class="fn">visit_meta_name_value</a>(&mut self, i: &'ast <a href="../struct.MetaNameValue.html" class="struct"
title="struct syn::MetaNameValue">MetaNameValue</a>)

</div>

<div id="method.visit_parenthesized_generic_arguments"
class="section method">

<a href="../../src/syn/gen/visit.rs.html#617-622"
class="src rightside">Source</a>

#### fn <a href="#method.visit_parenthesized_generic_arguments"
class="fn">visit_parenthesized_generic_arguments</a>( &mut self, i: &'ast <a href="../struct.ParenthesizedGenericArguments.html" class="struct"
title="struct syn::ParenthesizedGenericArguments">ParenthesizedGenericArguments</a>, )

</div>

<div id="method.visit_pat" class="section method">

<a href="../../src/syn/gen/visit.rs.html#625-627"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat" class="fn">visit_pat</a>(&mut self, i: &'ast <a href="../enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>)

</div>

<div id="method.visit_pat_ident" class="section method">

<a href="../../src/syn/gen/visit.rs.html#630-632"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_ident" class="fn">visit_pat_ident</a>(&mut self, i: &'ast <a href="../struct.PatIdent.html" class="struct"
title="struct syn::PatIdent">PatIdent</a>)

</div>

<div id="method.visit_pat_or" class="section method">

<a href="../../src/syn/gen/visit.rs.html#635-637"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_or" class="fn">visit_pat_or</a>(&mut self, i: &'ast <a href="../struct.PatOr.html" class="struct"
title="struct syn::PatOr">PatOr</a>)

</div>

<div id="method.visit_pat_paren" class="section method">

<a href="../../src/syn/gen/visit.rs.html#640-642"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_paren" class="fn">visit_pat_paren</a>(&mut self, i: &'ast <a href="../struct.PatParen.html" class="struct"
title="struct syn::PatParen">PatParen</a>)

</div>

<div id="method.visit_pat_reference" class="section method">

<a href="../../src/syn/gen/visit.rs.html#645-647"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_reference" class="fn">visit_pat_reference</a>(&mut self, i: &'ast <a href="../struct.PatReference.html" class="struct"
title="struct syn::PatReference">PatReference</a>)

</div>

<div id="method.visit_pat_rest" class="section method">

<a href="../../src/syn/gen/visit.rs.html#650-652"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_rest" class="fn">visit_pat_rest</a>(&mut self, i: &'ast <a href="../struct.PatRest.html" class="struct"
title="struct syn::PatRest">PatRest</a>)

</div>

<div id="method.visit_pat_slice" class="section method">

<a href="../../src/syn/gen/visit.rs.html#655-657"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_slice" class="fn">visit_pat_slice</a>(&mut self, i: &'ast <a href="../struct.PatSlice.html" class="struct"
title="struct syn::PatSlice">PatSlice</a>)

</div>

<div id="method.visit_pat_struct" class="section method">

<a href="../../src/syn/gen/visit.rs.html#660-662"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_struct" class="fn">visit_pat_struct</a>(&mut self, i: &'ast <a href="../struct.PatStruct.html" class="struct"
title="struct syn::PatStruct">PatStruct</a>)

</div>

<div id="method.visit_pat_tuple" class="section method">

<a href="../../src/syn/gen/visit.rs.html#665-667"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_tuple" class="fn">visit_pat_tuple</a>(&mut self, i: &'ast <a href="../struct.PatTuple.html" class="struct"
title="struct syn::PatTuple">PatTuple</a>)

</div>

<div id="method.visit_pat_tuple_struct" class="section method">

<a href="../../src/syn/gen/visit.rs.html#670-672"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_tuple_struct"
class="fn">visit_pat_tuple_struct</a>(&mut self, i: &'ast <a href="../struct.PatTupleStruct.html" class="struct"
title="struct syn::PatTupleStruct">PatTupleStruct</a>)

</div>

<div id="method.visit_pat_type" class="section method">

<a href="../../src/syn/gen/visit.rs.html#675-677"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_type" class="fn">visit_pat_type</a>(&mut self, i: &'ast <a href="../struct.PatType.html" class="struct"
title="struct syn::PatType">PatType</a>)

</div>

<div id="method.visit_pat_wild" class="section method">

<a href="../../src/syn/gen/visit.rs.html#680-682"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_wild" class="fn">visit_pat_wild</a>(&mut self, i: &'ast <a href="../struct.PatWild.html" class="struct"
title="struct syn::PatWild">PatWild</a>)

</div>

<div id="method.visit_path" class="section method">

<a href="../../src/syn/gen/visit.rs.html#685-687"
class="src rightside">Source</a>

#### fn <a href="#method.visit_path" class="fn">visit_path</a>(&mut self, i: &'ast <a href="../struct.Path.html" class="struct"
title="struct syn::Path">Path</a>)

</div>

<div id="method.visit_path_arguments" class="section method">

<a href="../../src/syn/gen/visit.rs.html#690-692"
class="src rightside">Source</a>

#### fn <a href="#method.visit_path_arguments"
class="fn">visit_path_arguments</a>(&mut self, i: &'ast <a href="../enum.PathArguments.html" class="enum"
title="enum syn::PathArguments">PathArguments</a>)

</div>

<div id="method.visit_path_segment" class="section method">

<a href="../../src/syn/gen/visit.rs.html#695-697"
class="src rightside">Source</a>

#### fn <a href="#method.visit_path_segment" class="fn">visit_path_segment</a>(&mut self, i: &'ast <a href="../struct.PathSegment.html" class="struct"
title="struct syn::PathSegment">PathSegment</a>)

</div>

<div id="method.visit_pointer_mutability" class="section method">

<a href="../../src/syn/gen/visit.rs.html#700-702"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pointer_mutability"
class="fn">visit_pointer_mutability</a>(&mut self, i: &'ast <a href="../enum.PointerMutability.html" class="enum"
title="enum syn::PointerMutability">PointerMutability</a>)

</div>

<div id="method.visit_precise_capture" class="section method">

<a href="../../src/syn/gen/visit.rs.html#705-707"
class="src rightside">Source</a>

#### fn <a href="#method.visit_precise_capture"
class="fn">visit_precise_capture</a>(&mut self, i: &'ast <a href="../struct.PreciseCapture.html" class="struct"
title="struct syn::PreciseCapture">PreciseCapture</a>)

</div>

<div id="method.visit_predicate_lifetime" class="section method">

<a href="../../src/syn/gen/visit.rs.html#710-712"
class="src rightside">Source</a>

#### fn <a href="#method.visit_predicate_lifetime"
class="fn">visit_predicate_lifetime</a>(&mut self, i: &'ast <a href="../struct.PredicateLifetime.html" class="struct"
title="struct syn::PredicateLifetime">PredicateLifetime</a>)

</div>

<div id="method.visit_predicate_type" class="section method">

<a href="../../src/syn/gen/visit.rs.html#715-717"
class="src rightside">Source</a>

#### fn <a href="#method.visit_predicate_type"
class="fn">visit_predicate_type</a>(&mut self, i: &'ast <a href="../struct.PredicateType.html" class="struct"
title="struct syn::PredicateType">PredicateType</a>)

</div>

<div id="method.visit_qself" class="section method">

<a href="../../src/syn/gen/visit.rs.html#720-722"
class="src rightside">Source</a>

#### fn <a href="#method.visit_qself" class="fn">visit_qself</a>(&mut self, i: &'ast <a href="../struct.QSelf.html" class="struct"
title="struct syn::QSelf">QSelf</a>)

</div>

<div id="method.visit_range_limits" class="section method">

<a href="../../src/syn/gen/visit.rs.html#725-727"
class="src rightside">Source</a>

#### fn <a href="#method.visit_range_limits" class="fn">visit_range_limits</a>(&mut self, i: &'ast <a href="../enum.RangeLimits.html" class="enum"
title="enum syn::RangeLimits">RangeLimits</a>)

</div>

<div id="method.visit_receiver" class="section method">

<a href="../../src/syn/gen/visit.rs.html#730-732"
class="src rightside">Source</a>

#### fn <a href="#method.visit_receiver" class="fn">visit_receiver</a>(&mut self, i: &'ast <a href="../struct.Receiver.html" class="struct"
title="struct syn::Receiver">Receiver</a>)

</div>

<div id="method.visit_return_type" class="section method">

<a href="../../src/syn/gen/visit.rs.html#735-737"
class="src rightside">Source</a>

#### fn <a href="#method.visit_return_type" class="fn">visit_return_type</a>(&mut self, i: &'ast <a href="../enum.ReturnType.html" class="enum"
title="enum syn::ReturnType">ReturnType</a>)

</div>

<div id="method.visit_signature" class="section method">

<a href="../../src/syn/gen/visit.rs.html#740-742"
class="src rightside">Source</a>

#### fn <a href="#method.visit_signature" class="fn">visit_signature</a>(&mut self, i: &'ast <a href="../struct.Signature.html" class="struct"
title="struct syn::Signature">Signature</a>)

</div>

<div id="method.visit_span" class="section method">

<a href="../../src/syn/gen/visit.rs.html#743"
class="src rightside">Source</a>

#### fn <a href="#method.visit_span" class="fn">visit_span</a>(&mut self, i: &<a href="../../proc_macro2/struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>)

</div>

<div id="method.visit_static_mutability" class="section method">

<a href="../../src/syn/gen/visit.rs.html#746-748"
class="src rightside">Source</a>

#### fn <a href="#method.visit_static_mutability"
class="fn">visit_static_mutability</a>(&mut self, i: &'ast <a href="../enum.StaticMutability.html" class="enum"
title="enum syn::StaticMutability">StaticMutability</a>)

</div>

<div id="method.visit_stmt" class="section method">

<a href="../../src/syn/gen/visit.rs.html#751-753"
class="src rightside">Source</a>

#### fn <a href="#method.visit_stmt" class="fn">visit_stmt</a>(&mut self, i: &'ast <a href="../enum.Stmt.html" class="enum" title="enum syn::Stmt">Stmt</a>)

</div>

<div id="method.visit_stmt_macro" class="section method">

<a href="../../src/syn/gen/visit.rs.html#756-758"
class="src rightside">Source</a>

#### fn <a href="#method.visit_stmt_macro" class="fn">visit_stmt_macro</a>(&mut self, i: &'ast <a href="../struct.StmtMacro.html" class="struct"
title="struct syn::StmtMacro">StmtMacro</a>)

</div>

<div id="method.visit_token_stream" class="section method">

<a href="../../src/syn/gen/visit.rs.html#759"
class="src rightside">Source</a>

#### fn <a href="#method.visit_token_stream" class="fn">visit_token_stream</a>(&mut self, i: &'ast <a href="../../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

<div id="method.visit_trait_bound" class="section method">

<a href="../../src/syn/gen/visit.rs.html#762-764"
class="src rightside">Source</a>

#### fn <a href="#method.visit_trait_bound" class="fn">visit_trait_bound</a>(&mut self, i: &'ast <a href="../struct.TraitBound.html" class="struct"
title="struct syn::TraitBound">TraitBound</a>)

</div>

<div id="method.visit_trait_bound_modifier" class="section method">

<a href="../../src/syn/gen/visit.rs.html#767-769"
class="src rightside">Source</a>

#### fn <a href="#method.visit_trait_bound_modifier"
class="fn">visit_trait_bound_modifier</a>(&mut self, i: &'ast <a href="../enum.TraitBoundModifier.html" class="enum"
title="enum syn::TraitBoundModifier">TraitBoundModifier</a>)

</div>

<div id="method.visit_trait_item" class="section method">

<a href="../../src/syn/gen/visit.rs.html#772-774"
class="src rightside">Source</a>

#### fn <a href="#method.visit_trait_item" class="fn">visit_trait_item</a>(&mut self, i: &'ast <a href="../enum.TraitItem.html" class="enum"
title="enum syn::TraitItem">TraitItem</a>)

</div>

<div id="method.visit_trait_item_const" class="section method">

<a href="../../src/syn/gen/visit.rs.html#777-779"
class="src rightside">Source</a>

#### fn <a href="#method.visit_trait_item_const"
class="fn">visit_trait_item_const</a>(&mut self, i: &'ast <a href="../struct.TraitItemConst.html" class="struct"
title="struct syn::TraitItemConst">TraitItemConst</a>)

</div>

<div id="method.visit_trait_item_fn" class="section method">

<a href="../../src/syn/gen/visit.rs.html#782-784"
class="src rightside">Source</a>

#### fn <a href="#method.visit_trait_item_fn" class="fn">visit_trait_item_fn</a>(&mut self, i: &'ast <a href="../struct.TraitItemFn.html" class="struct"
title="struct syn::TraitItemFn">TraitItemFn</a>)

</div>

<div id="method.visit_trait_item_macro" class="section method">

<a href="../../src/syn/gen/visit.rs.html#787-789"
class="src rightside">Source</a>

#### fn <a href="#method.visit_trait_item_macro"
class="fn">visit_trait_item_macro</a>(&mut self, i: &'ast <a href="../struct.TraitItemMacro.html" class="struct"
title="struct syn::TraitItemMacro">TraitItemMacro</a>)

</div>

<div id="method.visit_trait_item_type" class="section method">

<a href="../../src/syn/gen/visit.rs.html#792-794"
class="src rightside">Source</a>

#### fn <a href="#method.visit_trait_item_type"
class="fn">visit_trait_item_type</a>(&mut self, i: &'ast <a href="../struct.TraitItemType.html" class="struct"
title="struct syn::TraitItemType">TraitItemType</a>)

</div>

<div id="method.visit_type" class="section method">

<a href="../../src/syn/gen/visit.rs.html#797-799"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type" class="fn">visit_type</a>(&mut self, i: &'ast <a href="../enum.Type.html" class="enum" title="enum syn::Type">Type</a>)

</div>

<div id="method.visit_type_array" class="section method">

<a href="../../src/syn/gen/visit.rs.html#802-804"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_array" class="fn">visit_type_array</a>(&mut self, i: &'ast <a href="../struct.TypeArray.html" class="struct"
title="struct syn::TypeArray">TypeArray</a>)

</div>

<div id="method.visit_type_bare_fn" class="section method">

<a href="../../src/syn/gen/visit.rs.html#807-809"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_bare_fn" class="fn">visit_type_bare_fn</a>(&mut self, i: &'ast <a href="../struct.TypeBareFn.html" class="struct"
title="struct syn::TypeBareFn">TypeBareFn</a>)

</div>

<div id="method.visit_type_group" class="section method">

<a href="../../src/syn/gen/visit.rs.html#812-814"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_group" class="fn">visit_type_group</a>(&mut self, i: &'ast <a href="../struct.TypeGroup.html" class="struct"
title="struct syn::TypeGroup">TypeGroup</a>)

</div>

<div id="method.visit_type_impl_trait" class="section method">

<a href="../../src/syn/gen/visit.rs.html#817-819"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_impl_trait"
class="fn">visit_type_impl_trait</a>(&mut self, i: &'ast <a href="../struct.TypeImplTrait.html" class="struct"
title="struct syn::TypeImplTrait">TypeImplTrait</a>)

</div>

<div id="method.visit_type_infer" class="section method">

<a href="../../src/syn/gen/visit.rs.html#822-824"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_infer" class="fn">visit_type_infer</a>(&mut self, i: &'ast <a href="../struct.TypeInfer.html" class="struct"
title="struct syn::TypeInfer">TypeInfer</a>)

</div>

<div id="method.visit_type_macro" class="section method">

<a href="../../src/syn/gen/visit.rs.html#827-829"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_macro" class="fn">visit_type_macro</a>(&mut self, i: &'ast <a href="../struct.TypeMacro.html" class="struct"
title="struct syn::TypeMacro">TypeMacro</a>)

</div>

<div id="method.visit_type_never" class="section method">

<a href="../../src/syn/gen/visit.rs.html#832-834"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_never" class="fn">visit_type_never</a>(&mut self, i: &'ast <a href="../struct.TypeNever.html" class="struct"
title="struct syn::TypeNever">TypeNever</a>)

</div>

<div id="method.visit_type_param" class="section method">

<a href="../../src/syn/gen/visit.rs.html#837-839"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_param" class="fn">visit_type_param</a>(&mut self, i: &'ast <a href="../struct.TypeParam.html" class="struct"
title="struct syn::TypeParam">TypeParam</a>)

</div>

<div id="method.visit_type_param_bound" class="section method">

<a href="../../src/syn/gen/visit.rs.html#842-844"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_param_bound"
class="fn">visit_type_param_bound</a>(&mut self, i: &'ast <a href="../enum.TypeParamBound.html" class="enum"
title="enum syn::TypeParamBound">TypeParamBound</a>)

</div>

<div id="method.visit_type_paren" class="section method">

<a href="../../src/syn/gen/visit.rs.html#847-849"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_paren" class="fn">visit_type_paren</a>(&mut self, i: &'ast <a href="../struct.TypeParen.html" class="struct"
title="struct syn::TypeParen">TypeParen</a>)

</div>

<div id="method.visit_type_path" class="section method">

<a href="../../src/syn/gen/visit.rs.html#852-854"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_path" class="fn">visit_type_path</a>(&mut self, i: &'ast <a href="../struct.TypePath.html" class="struct"
title="struct syn::TypePath">TypePath</a>)

</div>

<div id="method.visit_type_ptr" class="section method">

<a href="../../src/syn/gen/visit.rs.html#857-859"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_ptr" class="fn">visit_type_ptr</a>(&mut self, i: &'ast <a href="../struct.TypePtr.html" class="struct"
title="struct syn::TypePtr">TypePtr</a>)

</div>

<div id="method.visit_type_reference" class="section method">

<a href="../../src/syn/gen/visit.rs.html#862-864"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_reference"
class="fn">visit_type_reference</a>(&mut self, i: &'ast <a href="../struct.TypeReference.html" class="struct"
title="struct syn::TypeReference">TypeReference</a>)

</div>

<div id="method.visit_type_slice" class="section method">

<a href="../../src/syn/gen/visit.rs.html#867-869"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_slice" class="fn">visit_type_slice</a>(&mut self, i: &'ast <a href="../struct.TypeSlice.html" class="struct"
title="struct syn::TypeSlice">TypeSlice</a>)

</div>

<div id="method.visit_type_trait_object" class="section method">

<a href="../../src/syn/gen/visit.rs.html#872-874"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_trait_object"
class="fn">visit_type_trait_object</a>(&mut self, i: &'ast <a href="../struct.TypeTraitObject.html" class="struct"
title="struct syn::TypeTraitObject">TypeTraitObject</a>)

</div>

<div id="method.visit_type_tuple" class="section method">

<a href="../../src/syn/gen/visit.rs.html#877-879"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_tuple" class="fn">visit_type_tuple</a>(&mut self, i: &'ast <a href="../struct.TypeTuple.html" class="struct"
title="struct syn::TypeTuple">TypeTuple</a>)

</div>

<div id="method.visit_un_op" class="section method">

<a href="../../src/syn/gen/visit.rs.html#882-884"
class="src rightside">Source</a>

#### fn <a href="#method.visit_un_op" class="fn">visit_un_op</a>(&mut self, i: &'ast <a href="../enum.UnOp.html" class="enum" title="enum syn::UnOp">UnOp</a>)

</div>

<div id="method.visit_use_glob" class="section method">

<a href="../../src/syn/gen/visit.rs.html#887-889"
class="src rightside">Source</a>

#### fn <a href="#method.visit_use_glob" class="fn">visit_use_glob</a>(&mut self, i: &'ast <a href="../struct.UseGlob.html" class="struct"
title="struct syn::UseGlob">UseGlob</a>)

</div>

<div id="method.visit_use_group" class="section method">

<a href="../../src/syn/gen/visit.rs.html#892-894"
class="src rightside">Source</a>

#### fn <a href="#method.visit_use_group" class="fn">visit_use_group</a>(&mut self, i: &'ast <a href="../struct.UseGroup.html" class="struct"
title="struct syn::UseGroup">UseGroup</a>)

</div>

<div id="method.visit_use_name" class="section method">

<a href="../../src/syn/gen/visit.rs.html#897-899"
class="src rightside">Source</a>

#### fn <a href="#method.visit_use_name" class="fn">visit_use_name</a>(&mut self, i: &'ast <a href="../struct.UseName.html" class="struct"
title="struct syn::UseName">UseName</a>)

</div>

<div id="method.visit_use_path" class="section method">

<a href="../../src/syn/gen/visit.rs.html#902-904"
class="src rightside">Source</a>

#### fn <a href="#method.visit_use_path" class="fn">visit_use_path</a>(&mut self, i: &'ast <a href="../struct.UsePath.html" class="struct"
title="struct syn::UsePath">UsePath</a>)

</div>

<div id="method.visit_use_rename" class="section method">

<a href="../../src/syn/gen/visit.rs.html#907-909"
class="src rightside">Source</a>

#### fn <a href="#method.visit_use_rename" class="fn">visit_use_rename</a>(&mut self, i: &'ast <a href="../struct.UseRename.html" class="struct"
title="struct syn::UseRename">UseRename</a>)

</div>

<div id="method.visit_use_tree" class="section method">

<a href="../../src/syn/gen/visit.rs.html#912-914"
class="src rightside">Source</a>

#### fn <a href="#method.visit_use_tree" class="fn">visit_use_tree</a>(&mut self, i: &'ast <a href="../enum.UseTree.html" class="enum"
title="enum syn::UseTree">UseTree</a>)

</div>

<div id="method.visit_variadic" class="section method">

<a href="../../src/syn/gen/visit.rs.html#917-919"
class="src rightside">Source</a>

#### fn <a href="#method.visit_variadic" class="fn">visit_variadic</a>(&mut self, i: &'ast <a href="../struct.Variadic.html" class="struct"
title="struct syn::Variadic">Variadic</a>)

</div>

<div id="method.visit_variant" class="section method">

<a href="../../src/syn/gen/visit.rs.html#922-924"
class="src rightside">Source</a>

#### fn <a href="#method.visit_variant" class="fn">visit_variant</a>(&mut self, i: &'ast <a href="../struct.Variant.html" class="struct"
title="struct syn::Variant">Variant</a>)

</div>

<div id="method.visit_vis_restricted" class="section method">

<a href="../../src/syn/gen/visit.rs.html#927-929"
class="src rightside">Source</a>

#### fn <a href="#method.visit_vis_restricted"
class="fn">visit_vis_restricted</a>(&mut self, i: &'ast <a href="../struct.VisRestricted.html" class="struct"
title="struct syn::VisRestricted">VisRestricted</a>)

</div>

<div id="method.visit_visibility" class="section method">

<a href="../../src/syn/gen/visit.rs.html#932-934"
class="src rightside">Source</a>

#### fn <a href="#method.visit_visibility" class="fn">visit_visibility</a>(&mut self, i: &'ast <a href="../enum.Visibility.html" class="enum"
title="enum syn::Visibility">Visibility</a>)

</div>

<div id="method.visit_where_clause" class="section method">

<a href="../../src/syn/gen/visit.rs.html#937-939"
class="src rightside">Source</a>

#### fn <a href="#method.visit_where_clause" class="fn">visit_where_clause</a>(&mut self, i: &'ast <a href="../struct.WhereClause.html" class="struct"
title="struct syn::WhereClause">WhereClause</a>)

</div>

<div id="method.visit_where_predicate" class="section method">

<a href="../../src/syn/gen/visit.rs.html#942-944"
class="src rightside">Source</a>

#### fn <a href="#method.visit_where_predicate"
class="fn">visit_where_predicate</a>(&mut self, i: &'ast <a href="../enum.WherePredicate.html" class="enum"
title="enum syn::WherePredicate">WherePredicate</a>)

</div>

</div>

## Implementors<a href="#implementors" class="anchor">§</a>

<div id="implementors-list">

</div>

</div>

</div>
