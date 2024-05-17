-- [COPY]

-- gsSmokeByType
COPY raw_data.gsSmokeByType
FROM 's3://de3-pjt2/csv/Gastric05-gsSmokeByType.csv'
credentials 'aws_iam_role=arn:aws:iam::339712859001:role/redshift.read.s3'
timeformat 'auto'
delimiter ','
IGNOREHEADER 1;

-- voSmokeByType
COPY raw_data.voSmokeByType
FROM 's3://de3-pjt2/csv/Colon05-voSmokeByType.csv'
credentials 'aws_iam_role=arn:aws:iam::339712859001:role/redshift.read.s3'
timeformat 'auto'
delimiter ','
IGNOREHEADER 1;

-- lvSmokeByType
COPY raw_data.lvSmokeByType
FROM 's3://de3-pjt2/csv/Liver05-lvSmokeByType.csv'
credentials 'aws_iam_role=arn:aws:iam::339712859001:role/redshift.read.s3'
timeformat 'auto'
delimiter ','
IGNOREHEADER 1;

-- chSmokeByType
COPY raw_data.chSmokeByType
FROM 's3://de3-pjt2/csv/Cholan05-chSmokeByType.csv'
credentials 'aws_iam_role=arn:aws:iam::339712859001:role/redshift.read.s3'
timeformat 'auto'
delimiter ','
IGNOREHEADER 1;

-- pnSmokeByType
COPY raw_data.pnSmokeByType
FROM 's3://de3-pjt2/csv/Pancreatic05-pnSmokeByType.csv'
credentials 'aws_iam_role=arn:aws:iam::339712859001:role/redshift.read.s3'
timeformat 'auto'
delimiter ','
IGNOREHEADER 1;

-- luSmokeByType
COPY raw_data.luSmokeByType
FROM 's3://de3-pjt2/csv/Lung05-luSmokeByType.csv'
credentials 'aws_iam_role=arn:aws:iam::339712859001:role/redshift.read.s3'
timeformat 'auto'
delimiter ','
IGNOREHEADER 1;

-- prSmokeByType
COPY raw_data.prSmokeByType
FROM 's3://de3-pjt2/csv/Prostate05-prSmokeByType.csv'
credentials 'aws_iam_role=arn:aws:iam::339712859001:role/redshift.read.s3'
timeformat 'auto'
delimiter ','
IGNOREHEADER 1;

-- kiSmokeByType
COPY raw_data.kiSmokeByType
FROM 's3://de3-pjt2/csv/Kidney05-kiSmokeByType.csv'
credentials 'aws_iam_role=arn:aws:iam::339712859001:role/redshift.read.s3'
timeformat 'auto'
delimiter ','
IGNOREHEADER 1;

-- ----------------------------------------------------------------------

-- gsPastSmokeByType
COPY raw_data.gsPastSmokeByType
FROM 's3://de3-pjt2/csv/Gastric06-gsPastSmokeByType.csv'
credentials 'aws_iam_role=arn:aws:iam::339712859001:role/redshift.read.s3'
timeformat 'auto'
delimiter ','
IGNOREHEADER 1;

-- voPastSmokeByType
COPY raw_data.voPastSmokeByType
FROM 's3://de3-pjt2/csv/Colon06-voPastSmokeByType.csv'
credentials 'aws_iam_role=arn:aws:iam::339712859001:role/redshift.read.s3'
timeformat 'auto'
delimiter ','
IGNOREHEADER 1;

-- lvPastSmokeByType
COPY raw_data.lvPastSmokeByType
FROM 's3://de3-pjt2/csv/Liver06-lvPastSmokeByType.csv'
credentials 'aws_iam_role=arn:aws:iam::339712859001:role/redshift.read.s3'
timeformat 'auto'
delimiter ','
IGNOREHEADER 1;

-- chPastSmokeByType
COPY raw_data.chPastSmokeByType
FROM 's3://de3-pjt2/csv/Cholan06-chPastSmokeByType.csv'
credentials 'aws_iam_role=arn:aws:iam::339712859001:role/redshift.read.s3'
timeformat 'auto'
delimiter ','
IGNOREHEADER 1;

-- pnPastSmokeByType
COPY raw_data.pnPastSmokeByType
FROM 's3://de3-pjt2/csv/Pancreatic06-pnPastSmokeByType.csv'
credentials 'aws_iam_role=arn:aws:iam::339712859001:role/redshift.read.s3'
timeformat 'auto'
delimiter ','
IGNOREHEADER 1;

-- luPastSmokeByType
COPY raw_data.luPastSmokeByType
FROM 's3://de3-pjt2/csv/Lung06-luPastSmokeByType.csv'
credentials 'aws_iam_role=arn:aws:iam::339712859001:role/redshift.read.s3'
timeformat 'auto'
delimiter ','
IGNOREHEADER 1;

-- prPastSmokeByType
COPY raw_data.prPastSmokeByType
FROM 's3://de3-pjt2/csv/Prostate06-prPastSmokeByType.csv'
credentials 'aws_iam_role=arn:aws:iam::339712859001:role/redshift.read.s3'
timeformat 'auto'
delimiter ','
IGNOREHEADER 1;

-- kiPastSmokeByType
COPY raw_data.kiPastSmokeByType
FROM 's3://de3-pjt2/csv/Kidney06-kiPastSmokeByType.csv'
credentials 'aws_iam_role=arn:aws:iam::339712859001:role/redshift.read.s3'
timeformat 'auto'
delimiter ','
IGNOREHEADER 1;

-- ----------------------------------------------------------------------

-- gsAlchbyType
COPY raw_data.gsAlchbyType
FROM 's3://de3-pjt2/csv/Gastric04-gsAlchbyType.csv'
credentials 'aws_iam_role=arn:aws:iam::339712859001:role/redshift.read.s3'
timeformat 'auto'
delimiter ','
IGNOREHEADER 1;

-- voAlchbyType
COPY raw_data.voAlchbyType
FROM 's3://de3-pjt2/csv/Colon04-voAlchbyType.csv'
credentials 'aws_iam_role=arn:aws:iam::339712859001:role/redshift.read.s3'
timeformat 'auto'
delimiter ','
IGNOREHEADER 1;

-- lvAlchbyType
COPY raw_data.lvAlchbyType
FROM 's3://de3-pjt2/csv/Liver04-lvAlchbyType.csv'
credentials 'aws_iam_role=arn:aws:iam::339712859001:role/redshift.read.s3'
timeformat 'auto'
delimiter ','
IGNOREHEADER 1;

-- chAlchbyType
COPY raw_data.chAlchbyType
FROM 's3://de3-pjt2/csv/Cholan04-chAlchbyType.csv'
credentials 'aws_iam_role=arn:aws:iam::339712859001:role/redshift.read.s3'
timeformat 'auto'
delimiter ','
IGNOREHEADER 1;

-- pnAlchbyType
COPY raw_data.pnAlchbyType
FROM 's3://de3-pjt2/csv/Pancreatic04-pnAlchbyType.csv'
credentials 'aws_iam_role=arn:aws:iam::339712859001:role/redshift.read.s3'
timeformat 'auto'
delimiter ','
IGNOREHEADER 1;

-- luAlchbyType
COPY raw_data.luAlchbyType
FROM 's3://de3-pjt2/csv/Lung04-luAlchbyType.csv'
credentials 'aws_iam_role=arn:aws:iam::339712859001:role/redshift.read.s3'
timeformat 'auto'
delimiter ','
IGNOREHEADER 1;

-- prAlchbyType
COPY raw_data.prAlchbyType
FROM 's3://de3-pjt2/csv/Prostate04-prAlchbyType.csv'
credentials 'aws_iam_role=arn:aws:iam::339712859001:role/redshift.read.s3'
timeformat 'auto'
delimiter ','
IGNOREHEADER 1;

-- kiAlchbyType
COPY raw_data.kiAlchbyType
FROM 's3://de3-pjt2/csv/Kidney04-kiAlchbyType.csv'
credentials 'aws_iam_role=arn:aws:iam::339712859001:role/redshift.read.s3'
timeformat 'auto'
delimiter ','
IGNOREHEADER 1;

-- ==============================================================================

-- 연도별_암_종류_발생자_수.json
-- CANCER_BY_YEAR : 완료
COPY analytics.CANCER_BY_YEAR
FROM 's3://de3-pjt2/csv/CANCER_BY_YEAR.csv'
credentials 'aws_iam_role=arn:aws:iam::339712859001:role/redshift.read.s3'
timeformat 'auto'
delimiter ','
IGNOREHEADER 1
removequotes
emptyasnull
blanksasnull;

-- 연도별_음주자_비율.json
-- ALCH_RATE_BY_YEAR : 완료
COPY analytics.ALCH_RATE_BY_YEAR
FROM 's3://de3-pjt2/csv/ALCH_RATE_BY_YEAR.csv'
credentials 'aws_iam_role=arn:aws:iam::339712859001:role/redshift.read.s3'
timeformat 'auto'
delimiter ','
IGNOREHEADER 1
removequotes
emptyasnull
blanksasnull;

-- 연도별_흡연자_비율.json
-- SMOKING_RATE_BY_YEAR : 완료
COPY analytics.SMOKING_RATE_BY_YEAR
FROM 's3://de3-pjt2/csv/SMOKING_RATE_BY_YEAR.csv'
credentials 'aws_iam_role=arn:aws:iam::339712859001:role/redshift.read.s3'
timeformat 'auto'
delimiter ','
IGNOREHEADER 1
removequotes
emptyasnull
blanksasnull;

-- 연령대별_발생자_수.json
-- REGION_BY_AGE (in raw_data) : 완료
COPY raw_data.REGION_BY_AGE
FROM 's3://de3-pjt2/csv/REGION_BY_AGE.csv'
credentials 'aws_iam_role=arn:aws:iam::339712859001:role/redshift.read.s3'
timeformat 'auto'
delimiter ','
IGNOREHEADER 1;

-- 지역별_암_발생자_수.json
-- CANCER_BY_REGION : 완료
COPY analytics.CANCER_BY_REGION
FROM 's3://de3-pjt2/csv/CANCER_BY_REGION.csv'
credentials 'aws_iam_role=arn:aws:iam::339712859001:role/redshift.read.s3'
timeformat 'auto'
delimiter ','
IGNOREHEADER 1;

-- 가인님 S3에 직접 csv파일 추가
-- CANCER_BY_AGE : 완료
COPY analytics.CANCER_BY_AGE
FROM 's3://de3-pjt2/csv/CANCER_BY_AGE.csv'
credentials 'aws_iam_role=arn:aws:iam::339712859001:role/redshift.read.s3'
timeformat 'auto'
delimiter ','
IGNOREHEADER 1;