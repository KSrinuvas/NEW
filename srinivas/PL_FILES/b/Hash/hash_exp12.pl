#!/usr/bin/perl -w
use strict;
my %DAYS = (
    'Sun' => 0,
    'Mon' => 1,
    'Tue' => 2,
    'Wed' => 3,
    'Thu' => 4,
    'Fri' => 5,
    'Sat' => 6,
);

my @days = ("Tue", "Sat", "Wed", "Fri", "Mon");

my @ss = sort {$DAYS{$a} <=> $DAYS{$b}} @days;
print"@days\n";
print"@ss\n";



my @aa = sort {$DAYS{$a} <=> $DAYS{$b}} keys %DAYS;
print"@aa\n";


=c
sub sort_days {
    # $a and $b will be automatically defined by sort().
    # Look up the position of the day in the week
    # using the DAYS hash.
    my $x = $DAYS{$a};
    my $y = $DAYS{$b};
    
    # Now we can just compare $x and $y. Note, it
    # would be simpler in this case to use the <=>
    # operator.
    if($x < $y) {
        return -1;
    }
    elsif($x > $y) {
        return 1;
    }
    else {
        return 0;
    }
}

sub main
{
    my @days = ("Tue", "Sat", "Wed", "Fri", "Mon");
    
    # Sort days in order using a sort algorithm
    # contained in a function.
    @days = sort sort_days @days;
    
    # Instead, here we could just do this:
    # @days = sort {$DAYS{$a} <=> $DAYS{$b}} @days;
    
    foreach my $day(@days) {
        print "$day\n";
    }
}



main();

=cut



my %DA = (
    'Wed' => 3,
    'Mon' => 1,
    'Thu' => 4,
    'Tue' => 2,
    'Sun' => 0,
    'Fri' => 5,
    'Sat' => 6,
);

my @cc = keys %DA;
my @bb = sort {$DA{$a} <=> $DA{$b}} keys %DA;

print"@cc\n";
print"@bb\n";











