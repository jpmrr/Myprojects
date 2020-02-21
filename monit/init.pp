class monit {

  define build_home_conf {
    $home = "home${name}"
    file { "/etc/monit.d/check_${home}.conf":
      ensure  => present,
      owner   => root,
      group   => root,
      mode    => '0644',
      content => template('monit/check_home_conf.erb'),
      notify  => Service['monit']
    }
  }
  $monit_bin = '1'
  if ($::monit_bin) {
    package { 'monit-deps':
      ensure => 'installed',
    }

    service { 'monit':
      ensure     => running,
      enable     => true,
      hasrestart => true,
      require    => Package['monit-deps'],
    }


  case $::operatingsystem {
    'CentOS': {
      case $::lsbmajdistrelease {
        6: {
          $monit_conf = '/etc/monit.conf'
        }
        7: {
          $monit_conf = '/etc/monitrc'
        }
        default: {
          fail("Module ${module_name} is not supported on ${::operatingsystem} version ${::lsbmajdistreleae}")
        }
      }
    }
    'CloudLinux': {
      case $::lsbmajdistrelease {
        6: {
          $monit_conf = '/etc/monit.conf'
        }
        7:  {
          $monit_conf = '/etc/monitrc'
        }
        default: {
          fail("Module ${module_name} is not supported on ${::operatingsystem} version ${::lsbmajdistreleae}")
        }
      }
    }

    default: {
      fail("Module ${module_name} is not supported on Operating System ${::operatingsystem}")
    }
  }

   file { $monit_conf:
      ensure => file,
      owner  => root,
      group  => root,
      source => 'puppet:///modules/monit/etc/monit.conf',
      mode   => '0600',
      notify => Service['monit']
    }

    $def_home = '1'
    $num_homes = '2'
    notify{"The value of defhome is: ${def_home}": }
    notify{"The value of num home is: ${num_homes}": }

    case $::num_homes {
      1: {
        $home_list = [ '1' ]
      }
      2: {
        $home_list = [ '1', '2' ]
      }
      3: {
        $home_list = [ '1', '2', '3']
      }
      4: {
        $home_list = [ '1', '2', '3', '4' ]
      }
      5: {
        $home_list = [ '1', '2', '3', '4', '5' ]
      }
    }

    build_home_conf { $home_list:; }


    if $::def_home == '1' {
    $home = 'home'
      file { "/etc/monit.d/check_${home}.conf":
        ensure  => present,
        owner   => root,
        group   => root,
        mode    => '0644',
        content => template('monit/check_home_conf.erb'),
        notify  => Service['monit']
      }
    }
  }
}

