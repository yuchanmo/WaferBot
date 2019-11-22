CREATE TABLE [dbo].[cluster_result] (
    [cid]                     BIGINT         IDENTITY (1, 1) NOT NULL,
    [cluster_set_no]          INT            NOT NULL,
    [cluster_set_rev_no]      INT            NOT NULL,
    [cluster_set_result_info] NVARCHAR (MAX) NOT NULL,
    [regdate]                 DATETIME       CONSTRAINT [DF_cluster_result_regdate] DEFAULT (getdate()) NOT NULL,
    CONSTRAINT [PK_cluster_result] PRIMARY KEY CLUSTERED ([cid] ASC)
);

