from django.shortcuts import render

def index(request):
    return render(request, "securities_bank/index.html")

def guide(request):
    return render(request, "securities_bank/guide.html")

def bank(request):
    return render(request, "securities_bank/bank.html")

def securities(request):
    return render(request, "securities_bank/securities.html")

# =====================
# 银行卡科普
# =====================

# ===== 现金卡 =====
def cash_card(request):
    return render(
        request,
        "securities_bank/bank/cash_card.html"
    )


# ===== 借记卡 =====
def debit_card(request):
    return render(
        request,
        "securities_bank/bank/debit_card.html"
    )


# ===== 信用卡 =====
def credit_card(request):
    return render(
        request,
        "securities_bank/bank/credit_card.html"
    )


# =====================
# 主要银行
# =====================

# ===== 邮储银行 =====
def jp_bank(request):
    return render(
        request,
        "securities_bank/bank/jp/jp_bank.html"
    )

# ===== 乐天银行 =====
def rakuten_bank(request):
    return render(
        request,
        "securities_bank/bank/rakuten/rakuten_bank.html"
    )

# ===== paypay银行 =====
def paypay_bank(request):
    return render(
        request,
        "securities_bank/bank/paypay/paypay_bank.html"
    )

# ===== 三菱UFJ银行 =====
def mufg_bank(request):
    return render(
        request,
        "securities_bank/bank/mufg/mufg_bank.html"
    )

# ===== 三井住友银行 =====
def smbc_bank(request):
    return render(
        request,
        "securities_bank/bank/smbc/smbc_bank.html"
    )

# ===== 住信SBI银行 =====
def sbi_bank(request):
    return render(
        request,
        "securities_bank/bank/sbi/sbi_bank.html"
    )

#  ===== mizuho银行 =====
def mizuho_bank(request):
    return render(
        request,
        "securities_bank/bank/mizuho/mizuho_bank.html"
    )

#  ===== りそな银行 =====
def resona_bank(request):
    return render(
        request,
        "securities_bank/bank/resona/resona_bank.html"
    )


# =====================
# 证券公司
# =====================

# ===== SBI 证券 =====
def sbi_securities(request):
    return render(
        request,
        "securities_bank/securities/sbi_securities.html"
    )

# ===== 楽天证券 =====
def rakuten_securities(request):
    return render(
        request,
        "securities_bank/securities/rakuten_securities.html"
    )

# ===== Monex 证券 =====
def monex_securities(request):
    return render(
        request,
        "securities_bank/securities/monex_securities.html"
    )

# ===== moomoo 证券 =====
def moomoo_securities(request):
    return render(
        request,
        "securities_bank/securities/moomoo_securities.html"
    )

# ===== 松井证券 =====
def matsui_securities(request):
    return render(
        request,
        "securities_bank/securities/matsui_securities.html"
    )

# ===== 野村证券 =====
def nomura_securities(request):
    return render(
        request,
        "securities_bank/securities/nomura_securities.html"
    )