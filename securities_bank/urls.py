from django.urls import path
from . import views

urlpatterns = [

    path("", views.index, name="index"),

    path("guide/", views.guide, name="guide"),

    path("bank/", views.bank, name="bank"),

    path("securities/", views.securities, name="securities"),
    
    # =====================
    # 银行卡
    # =====================
    # ===== 现金卡 =====
    path(
        "bank/cash-card/",
        views.cash_card,
        name="cash_card"
    ),

    # ===== 借记卡 =====
    path(
        "bank/debit-card/",
        views.debit_card,
        name="debit_card"
    ),

    # ===== 信用卡 =====
    path(
        "bank/credit-card/",
        views.credit_card,
        name="credit_card"
    ),
    # =====================
    # 银行
    # =====================

    # ===== 邮储银行 =====
    path(
        "bank/jp-bank/",
        views.jp_bank,
        name="jp_bank"
    ),

    # ===== 乐天银行 =====
    path(
        "bank/rakuten-bank/",
        views.rakuten_bank,
        name="rakuten_bank"
    ),

    # ===== paypay银行 =====
    path(
        "bank/paypay-bank/",
        views.paypay_bank,
        name="paypay_bank"
    ),

    # ===== 三菱UFJ银行 =====
    path(
        "bank/mufg-bank/",
        views.mufg_bank,
        name="mufg_bank"
    ),

    # ===== 三井住友银行 =====
    path(
        "bank/smbc-bank/",
        views.smbc_bank,
        name="smbc_bank"
    ),

    # ===== 住信SBI银行 =====
    path(
        "bank/sbi-bank/",
        views.sbi_bank,
        name="sbi_bank"
    ),

    # =====================
    # 券商
    # =====================

    # ===== SBI 证券 =====
    path(
        "securities/sbi/",
        views.sbi_securities,
        name="sbi_securities"
    ),

    # ===== 楽天证券 =====
    path(
        "securities/rakuten/",
        views.rakuten_securities,
        name="rakuten_securities"
    ),

    # ===== Monex 证券 =====
    path(
        "securities/monex/",
        views.monex_securities,
        name="monex_securities"
    ),

    # ===== moomoo 证券 =====
    path(
        "securities/moomoo/",
        views.moomoo_securities,
        name="moomoo_securities"
    ),

    # ===== 松井证券 =====
    path(
        "securities/matsui/",
        views.matsui_securities,
        name="matsui_securities"
    ),

    # ===== 野村证券 =====
    path(
        "securities/nomura/",
        views.nomura_securities,
        name="nomura_securities"
    ),

    ]