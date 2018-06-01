# Generated by Django 2.0.5 on 2018-05-29 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('variants', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variant',
            name='snpeff_aa_change',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='snpeff_biotype',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='snpeff_codon_change',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='snpeff_exon_rank',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='snpeff_func_class',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='snpeff_gene_coding',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='snpeff_transcript_id',
        ),
        migrations.AddField(
            model_name='variant',
            name='snpeff_aa_pos_aa_len',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='snpeff_allele',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='snpeff_cdna_pos_cdna_len',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='snpeff_distance',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='snpeff_errors_warnings_info',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='snpeff_feature_id',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='snpeff_feature_type',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='snpeff_gene_id',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='snpeff_hgvs_c',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='snpeff_hgvs_p',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='snpeff_rank',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='variant',
            name='snpeff_transcript_biotype',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
    ]
