CREATE TABLE [dbo].[model_archive] (
    [model_id]        INT            NOT NULL,
    [model_type]      NVARCHAR (20)  NOT NULL,
    [model_file_name] NVARCHAR (MAX) NOT NULL,
    [is_active_model] BIT            NOT NULL,
    [regdate]         DATETIME       CONSTRAINT [DF_model_archive_regdate] DEFAULT (getdate()) NOT NULL,
    CONSTRAINT [PK_model_archive] PRIMARY KEY CLUSTERED ([model_id] ASC)
);

