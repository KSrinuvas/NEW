use strict;
use warnings;
use Module::Build;

my $builder = Module::Build->new(
    module_name         => 'Bio::Util::AA',
    license             => 'perl',
    dist_author         => 'Kevin Galinsky <kgalinsky plus cpan at mail dot com>',
    dist_version_from   => 'lib/Bio/Util/AA.pm',
    build_requires => {
        'Test::More' => 0,
    },
    add_to_cleanup      => [ 'Bio-Util-AA-*' ],
    create_makefile_pl => 'traditional',
);

$builder->create_build_script();
