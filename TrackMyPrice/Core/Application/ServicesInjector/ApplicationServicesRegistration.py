
from injector import Binder, singleton
from TrackMyPrice.Core.Application.Contracts.Factories.FormFactories.FormFactory import IFormFactory
from TrackMyPrice.Core.Application.Contracts.Repository import IImageBasicRepository
from TrackMyPrice.Core.Application.Contracts.UnitOfWork import IUnitOfWork
from TrackMyPrice.Core.Application.Contracts.UseCase import IUseCase
from TrackMyPrice.Core.Application.Factory.FormFactory import FormFactory
from TrackMyPrice.Core.Application.Persistence.UnitOfWork import UnitOfWork
from TrackMyPrice.Core.Application.UseCases.Image.CreateImageUseCase import CreateImageUseCase
from TrackMyPrice.Core.Application.UseCases.WriteUseCases.ScannedImage_UseCases import ScannedImageCreateUseCase
from TrackMyPrice.Infraestructure.Persistence.ImageBasicRepository import ImageBasicRepositoryImp

def ApplicationServicesInject(binder: Binder):
    binder.bind(IFormFactory, to=FormFactory, scope=singleton)
    #binder.bind(IUnitOfWork, to=UnitOfWork)
    binder.bind(IImageBasicRepository, to=ImageBasicRepositoryImp)
    binder.bind(IUseCase, to=CreateImageUseCase)

    return binder