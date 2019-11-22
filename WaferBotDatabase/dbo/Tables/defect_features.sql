CREATE TABLE [dbo].[defect_features] (
    [id]          BIGINT          IDENTITY (1, 1) NOT NULL,
    [model_id]    INT             NOT NULL,
    [is_abnormal] BIT             NOT NULL,
    [features]    VARBINARY (MAX) NOT NULL,
    [regdate]     DATETIME        CONSTRAINT [DF_defect_features_regdate] DEFAULT (getdate()) NOT NULL,
    CONSTRAINT [PK_defect_features] PRIMARY KEY CLUSTERED ([id] ASC)
);

