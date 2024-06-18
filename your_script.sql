CREATE TABLE pcos_infertility (
    "Sl. No" INTEGER PRIMARY KEY,
    "Patient File No." NUMERIC,
    "PCOS (Y/N)" NUMERIC,
    "Ibeta-HCG(mIU/mL)" NUMERIC, 
    "IIbeta-HCG(mIU/mL)" NUMERIC,
    "AMH(ng/mL)" NUMERIC
);

CREATE TABLE testonly (
    "H1" INTEGER PRIMARY KEY,
    "H2" NUMERIC,
    "H3" TEXT
);
