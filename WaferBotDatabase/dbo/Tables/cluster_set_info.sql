CREATE TABLE [dbo].[cluster_set_info] (
    [cluster_set_no]       INT             NOT NULL,
    [cluster_set_lot_list] VARBINARY (MAX) NOT NULL,
    [regdate]              DATETIME        CONSTRAINT [DF_cluster_set_info_regdate] DEFAULT (getdate()) NOT NULL
);

