#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libopenshot
Version  : 0.2.5
Release  : 1
URL      : https://github.com/OpenShot/libopenshot/archive/v0.2.5.tar.gz
Source0  : https://github.com/OpenShot/libopenshot/archive/v0.2.5.tar.gz
Summary  : A video editing, animation, and playback library for C++, Python, and Ruby
Group    : Development/Tools
License  : LGPL-3.0 MIT
Requires: libopenshot-lib = %{version}-%{release}
Requires: libopenshot-license = %{version}-%{release}
Requires: libopenshot-python = %{version}-%{release}
Requires: libopenshot-python3 = %{version}-%{release}
BuildRequires : ImageMagick
BuildRequires : buildreq-cmake
BuildRequires : cmake
BuildRequires : cppzmq-dev
BuildRequires : doxygen
BuildRequires : glibc-dev
BuildRequires : libopenshot-audio-dev
BuildRequires : libzmq-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(jsoncpp)
BuildRequires : pkgconfig(libavcodec)
BuildRequires : pkgconfig(libavdevice)
BuildRequires : pkgconfig(libavfilter)
BuildRequires : pkgconfig(libavformat)
BuildRequires : pkgconfig(libavutil)
BuildRequires : pkgconfig(libswresample)
BuildRequires : pkgconfig(libswscale)
BuildRequires : pkgconfig(libzmq)
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : qtmultimedia-dev
BuildRequires : ruby
BuildRequires : swig
BuildRequires : texlive

%description
OpenShot Video Library (libopenshot) is a free, open-source C++ library dedicated to
delivering high quality video editing, animation, and playback solutions to the
world.

%package dev
Summary: dev components for the libopenshot package.
Group: Development
Requires: libopenshot-lib = %{version}-%{release}
Provides: libopenshot-devel = %{version}-%{release}
Requires: libopenshot = %{version}-%{release}
Requires: libopenshot = %{version}-%{release}

%description dev
dev components for the libopenshot package.


%package lib
Summary: lib components for the libopenshot package.
Group: Libraries
Requires: libopenshot-license = %{version}-%{release}

%description lib
lib components for the libopenshot package.


%package license
Summary: license components for the libopenshot package.
Group: Default

%description license
license components for the libopenshot package.


%package python
Summary: python components for the libopenshot package.
Group: Default
Requires: libopenshot-python3 = %{version}-%{release}

%description python
python components for the libopenshot package.


%package python3
Summary: python3 components for the libopenshot package.
Group: Default
Requires: python3-core

%description python3
python3 components for the libopenshot package.


%prep
%setup -q -n libopenshot-0.2.5
cd %{_builddir}/libopenshot-0.2.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583269650
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1583269650
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libopenshot
cp %{_builddir}/libopenshot-0.2.5/COPYING %{buildroot}/usr/share/package-licenses/libopenshot/c09f9595f49b611cb4815dac18057910e5ff66b3
cp %{_builddir}/libopenshot-0.2.5/thirdparty/jsoncpp/LICENSE %{buildroot}/usr/share/package-licenses/libopenshot/d9bddd7f273bd065b5fdeb67afac0b26b6541a50
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/libopenshot/AudioBufferSource.h
/usr/include/libopenshot/AudioDeviceInfo.h
/usr/include/libopenshot/AudioReaderSource.h
/usr/include/libopenshot/AudioResampler.h
/usr/include/libopenshot/CacheBase.h
/usr/include/libopenshot/CacheDisk.h
/usr/include/libopenshot/CacheMemory.h
/usr/include/libopenshot/ChannelLayouts.h
/usr/include/libopenshot/ChunkReader.h
/usr/include/libopenshot/ChunkWriter.h
/usr/include/libopenshot/Clip.h
/usr/include/libopenshot/ClipBase.h
/usr/include/libopenshot/Color.h
/usr/include/libopenshot/Coordinate.h
/usr/include/libopenshot/CrashHandler.h
/usr/include/libopenshot/DecklinkInput.h
/usr/include/libopenshot/DecklinkOutput.h
/usr/include/libopenshot/DecklinkReader.h
/usr/include/libopenshot/DecklinkWriter.h
/usr/include/libopenshot/DummyReader.h
/usr/include/libopenshot/EffectBase.h
/usr/include/libopenshot/EffectInfo.h
/usr/include/libopenshot/Effects.h
/usr/include/libopenshot/Enums.h
/usr/include/libopenshot/Exceptions.h
/usr/include/libopenshot/FFmpegReader.h
/usr/include/libopenshot/FFmpegUtilities.h
/usr/include/libopenshot/FFmpegWriter.h
/usr/include/libopenshot/Fraction.h
/usr/include/libopenshot/Frame.h
/usr/include/libopenshot/FrameMapper.h
/usr/include/libopenshot/ImageReader.h
/usr/include/libopenshot/ImageWriter.h
/usr/include/libopenshot/Json.h
/usr/include/libopenshot/KeyFrame.h
/usr/include/libopenshot/MagickUtilities.h
/usr/include/libopenshot/OpenMPUtilities.h
/usr/include/libopenshot/OpenShot.h
/usr/include/libopenshot/OpenShotVersion.h
/usr/include/libopenshot/PlayerBase.h
/usr/include/libopenshot/Point.h
/usr/include/libopenshot/Profiles.h
/usr/include/libopenshot/Qt/AudioPlaybackThread.h
/usr/include/libopenshot/Qt/PlayerDemo.h
/usr/include/libopenshot/Qt/PlayerPrivate.h
/usr/include/libopenshot/Qt/VideoCacheThread.h
/usr/include/libopenshot/Qt/VideoPlaybackThread.h
/usr/include/libopenshot/Qt/VideoRenderWidget.h
/usr/include/libopenshot/Qt/VideoRenderer.h
/usr/include/libopenshot/QtHtmlReader.h
/usr/include/libopenshot/QtImageReader.h
/usr/include/libopenshot/QtPlayer.h
/usr/include/libopenshot/QtTextReader.h
/usr/include/libopenshot/ReaderBase.h
/usr/include/libopenshot/RendererBase.h
/usr/include/libopenshot/Settings.h
/usr/include/libopenshot/TextReader.h
/usr/include/libopenshot/Timeline.h
/usr/include/libopenshot/WriterBase.h
/usr/include/libopenshot/ZmqLogger.h
/usr/include/libopenshot/effects/Bars.h
/usr/include/libopenshot/effects/Blur.h
/usr/include/libopenshot/effects/Brightness.h
/usr/include/libopenshot/effects/ChromaKey.h
/usr/include/libopenshot/effects/ColorShift.h
/usr/include/libopenshot/effects/Crop.h
/usr/include/libopenshot/effects/Deinterlace.h
/usr/include/libopenshot/effects/Hue.h
/usr/include/libopenshot/effects/Mask.h
/usr/include/libopenshot/effects/Negate.h
/usr/include/libopenshot/effects/Pixelate.h
/usr/include/libopenshot/effects/Saturation.h
/usr/include/libopenshot/effects/Shift.h
/usr/include/libopenshot/effects/Wave.h
/usr/lib64/libopenshot.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libopenshot.so.0.2.5
/usr/lib64/libopenshot.so.19

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libopenshot/c09f9595f49b611cb4815dac18057910e5ff66b3
/usr/share/package-licenses/libopenshot/d9bddd7f273bd065b5fdeb67afac0b26b6541a50

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
